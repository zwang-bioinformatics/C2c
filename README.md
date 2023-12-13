# C2c: A tool that predicts Micro-C contact map based on Hi-C
Required Python packages:
  1. PyTorch
  2. Numpy
  3. cooler
  4. pickle

Required Hi-C files: All Hi-C files should be in the cooler ".cool" version. 

Steps:
  1. Generating input data for C2c.
  2. Using C2c to predict Micro-C data.
  3. Generating a ".cool" file for the predicted Micro-C data.

Examples:
1. Generating input data for C2c:
   
   "python generate_input_HiC.py ../../shared/micro_C/mES_cool/mES_HiC_mm10_mapq30_1kb_2.6B.cool 1000 16 fbt_16_1k.pkl".

For a given Hi-C cooler file, run "generate_input_HiC.py" to get the input file for the C2c model for predicting Micro-C data, where the first parameter "../../shared/micro_C/mES_cool/mES_HiC_mm10_mapq30_1kb_2.6B.cool" is the path of the Hi-C ".cool" file; the second "1000" is the resolution; the third parameter "16" is the chromosome; and the fourth parameter "fbt_16_1k.pkl" is the output file. All the parameters should be in the fixed order as in the example. The output file should be the ".pkl" version.

2. Using C2c to predict Micro-C data.

   "python pred_MicroC.py fbt_16_1k.pkl C2c_models/1kb_model pd_16_1k.pkl".

After obtaining the input file, run the "pred_MicroC.py" file to get the predicted Micro-C file, the output file of the C2c model is in the ".pkl" version, we provided two models in the "C2c_model" folder, one is for 1kb resolution, and the other is for 5kb resolution. From the example, the first parameter "fbt_16_1k.pkl" is the input Hi-C file getting from the previous step; the second parameter "C2c_models/1kb_model" is the 1kb C2c model; and the third parameter "pd_16_1k.pkl" is the output file from the C2c model. All the parameters should be in the fixed order as in the example. The output file should be the ".pkl" version.

3. Gnearting a ".cool" file for the predicted Micro-C data:

    "python create_pkl2cool.py pd_16_1k.pkl chr16 pd_16_1k.cool".

This step will generate a ".cool" for the predicted ".pkl" file. Run the "create_pkl2cool.py" file to do this. In the example, the first parameter "pd_16_1k.pkl" is the output file from Step 2; the second parameter "chr16" is the chromosome, "chr" should be added before the chromosome and should all be in lower case; the third parameter "pd_16_1k.cool" is the final ".cool" file. You can use cooler to extract the specific matrix from the predicted Micro-C data. 
