# SequenceCoverage
Scripts used for coverage analysis of pea aphid genome, The Moran Lab, The University of Texas at Austin.

readdepth.py    calculates the average read depth

coverage_rate.py    calculates the coverage rate

stdev.py    calculates the mean and standard deviations of depths of coverage of all 7 individual genomes sequenced

region.py    eliminates the regions whose depths of converage are 2 SDs or more away from the mean

normalization_med_ratio.py    i) normalises the depths of coverage, females with AL4f and males with AL4mw-B; ii) calculates post-normalisation median coverages for males and females; iii) calculates median(males) / median(females) for each interval; iv) plots the ratios (see normalization_med_ratio.png)

avg_cov.py    plots avg.depth of coverage of a scaffold vs. length of the scaffold

length_ratio.py    plots the male-over-female ratio of coverage (see normalization_med_ratio.py) vs. length of the scaffold

vcf_table.py    calculates statistics for heterozygous and homozygous SNPs from FreeBayes-generated, vcffilter-filtered vcf file

tab_delimit.py    converts a space-delimited file to a tab-delimited file

SNP_individual.py    extracts heterozygous SNPs of the given individual and saves the information as a BED-format file

Tools used:
Python 3 v.3.6.5
Matplotlib v.3.0.0
Bedtools v.2.26.0
Samtools v.0.1.19.96b5f2294a
Bcftools v.0.1.19.96b5f2294a
FreeBayes v.1.2.0

Contacts: 
For the author of above scripts, contact Hyunjin Park (hyunjin.park@utexas.edu)
For the first author of the paper, contact Dr. Yiyuan Li (yli@utexas.edu)
For the PI of the project, contact Dr. Nancy Moran (nancy.moran@austin.utexas.edu)
