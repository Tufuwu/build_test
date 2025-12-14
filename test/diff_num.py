import sys, glob
import numpy as np

ref_files = sorted(glob.glob(sys.argv[1] + "/*.prom"))
test_files = sorted(glob.glob(sys.argv[2] + "/*.prom"))

# Check that the number of files matches
if len(ref_files) != len(test_files):
    raise ValueError(
        f"Number of .prom files mismatch: ref={len(ref_files)}, test={len(test_files)}"
    )

for ref_path, test_path in zip(ref_files, test_files):
    ref = open(ref_path, "r").readlines()
    test = open(test_path, "r").readlines()

    val_ref = []
    val_test = []

    # extract last two columns
    for l in ref:
        parts = l.strip().split("\t")
        val_ref.append(float(parts[-1]))
        val_ref.append(float(parts[-2]))

    for l in test:
        parts = l.strip().split("\t")
        val_test.append(float(parts[-1]))
        val_test.append(float(parts[-2]))

    assert np.allclose(np.array(val_ref), np.array(val_test), atol=0.3), \
        f"{ref_path} and {test_path} differ too much!"