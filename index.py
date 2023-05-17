import musicRR
import openPDF
import transcriber
import categorisation
import os

output_folder = "Output\\"
output_file_name = "Peaks"

def output_clean():                             
    tmp = [f for f in next(os.walk("Output"))[2] if '.' not in f]
    for i in range(len(tmp)-1):
        os.rename("Output/"+tmp[i],"Output/tmp"+str(i)+".txt")
    for item in os.listdir("Output"):
        os.remove("Output/"+item)
def main(tuning_level, exclusion_level, min_tempo, max_tempo, filename, start_time):   
    output_clean()                    
    patient_bars = musicRR.main(filename, start_time)
    categorised_data = categorisation.main(patient_bars, tuning_level, exclusion_level, min_tempo, max_tempo)
    transcriber.main(categorised_data, output_folder+output_file_name+".ly")
    print("Generating...")
    openPDF.main()
    print("PDF file generated.")

if __name__ == "__main__":
    main()