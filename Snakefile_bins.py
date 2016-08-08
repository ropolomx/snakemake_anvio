import os

configfile: "config_bins.yaml"

ENV_ANVI = "source activate py3"

shell.prefix(ENV_ANVI + '; ')

# SAMPLES = ["A", "B"]
# ASSEMBLIES = ["X","Y"]
# CENTRIFUGE_BASE = "/home/jgsanders/miniconda/envs/anvio2/centrifuge"

rule all:
    input:
        expand("data/bins/{assembly}/picked_bins.txt", assembly=config["ASSEMBLIES"])

rule pick_bins:
    input:
        bins_dir = "data/{assembly}/{assembly}_SAMPLES-SUMMARY-refined/bin_by_bin"
        bins_fp = "data/{assembly}/{assembly}_SAMPLES-SUMMARY-refined/general_bins_summary.txt"
        cov_fp = "data/{assembly}/{assembly}_SAMPLES-SUMMARY-refined/bins_across_samples/mean_coverage.txt"
    output:
        bins_outdir = "data/bins/{assembly}"
        bins_info = "data/bins/{assembly}/picked_bins.txt"
    params:
        A = config["A"]
        C = config["C"]
        R = config["R"]
        N = config["N"]
        sample = config["SAMPLES"][wildcards.assembly]
    script:
        "pick_bins.py"
