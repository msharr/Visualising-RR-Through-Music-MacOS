#Writes and executes .ly file to generate PDF file
import os
from datetime import datetime

def tempo_highlight(ratio,i):
    if (ratio[i].tempo > ratio[i-1].tempo*1.2):
        colour = '\\staffHighlight "lightpink"'
        return colour
    elif (ratio[i].tempo < ratio[i-1].tempo*0.8):
        colour = '\\staffHighlight "lightsteelblue"'
        return colour
    else:
        return ""

def transcription_regions(ratio):  
    print("Data from: "+datetime.utcfromtimestamp(round(ratio[0].start)).strftime('%Y-%m-%d %H:%M')+" - "+datetime.utcfromtimestamp(round(ratio[len(ratio)-1].end)).strftime('%Y-%m-%d %H:%M'))                     
    transcription = []
    for i in range(len(ratio)-1):
        new_bar = True
        start = datetime.utcfromtimestamp(round(ratio[i].start)).strftime('%H:%M')
        end = datetime.utcfromtimestamp(round(ratio[i].end)).strftime('%H:%M')
        if i != 0:
            if ratio[i-1].notes == ratio[i].notes:
                transcription.append('\\addlyrics {"'+ str(start)+ ' - '+str(end)+' BPM = '+str(ratio[i].tempo)+'"}')
                new_bar = False
        if new_bar: 
            transcription.append("\\break")
            transcription.append("\\tempo \\markup{"+ str(start)+ " - "+str(end)+"} 4 = "+str(ratio[i].tempo))
            if ratio[i].notes == 0.4:
                transcription.append("\\time 7/8")
                transcription.append("\\repeat volta 2 {4.~ 4 4}  ")
            elif ratio[i].notes == 0.5:
                transcription.append("\\time 3/4")
                transcription.append("\\repeat volta 2 {2 4}  ")
            elif ratio[i].notes == 0.66:
                transcription.append("\\time 8/8 ")
                transcription.append("\\repeat volta 2 {4.~ 4 4.}  ")
            elif ratio[i].notes == 0.75:
                transcription.append("\\time 7/8")
                transcription.append("\\repeat volta 2 {2 4.}  ")
            elif ratio[i].notes == 0.8:
                transcription.append("\\time 9/8")
                transcription.append("\\repeat volta 2 {4.~ 4 2}  ")        
            elif ratio[i].notes == 1:
                transcription.append("\\time 2/2")
                transcription.append("\\repeat volta 2 {2 2}  ")
            elif ratio[i].notes == 1.25:
                transcription.append("\\time 9/8")
                transcription.append("\\repeat volta 2 {2 4.~ 4}  ")   
            elif ratio[i].notes == 1.33:
                transcription.append("\\time 7/8")
                transcription.append("\\repeat volta 2 {4. 2}  ")
            elif ratio[i].notes == 1.5:
                transcription.append("\\time 5/8")
                transcription.append("\\repeat volta 2 {4 4.}  ")
            elif ratio[i].notes == 1.75:
                transcription.append("\\time 11/8")
                transcription.append("\\repeat volta 2 {2 4.~ 2}  ")
            elif ratio[i].notes == 2:
                transcription.append("\\time 3/4")
                transcription.append("\\repeat volta 2 {4 2}  ")
            elif ratio[i].notes == 2.5:
                transcription.append("\\time 7/8")
                transcription.append("\\repeat volta 2 {4 4~ 4.}  ")          
    return transcription

def lilypond_create(transcription,file):             
    f = open (file,"w+")                 
    f.write('\\version "2.22.2"\n')
    f.write('\\new RhythmicStaff \with { instrumentName = #"RR ratios" }\n')
    f.write("\\new Voice {\n")
    f.write("\\hide Staff.Clef\n")
    f.write("\\numericTimeSignature\n")

    for i in range(len(transcription)):
        f.write(" "+transcription[i]+"\n")
    f.write("}")

def main(ratio_data, output_file):
    notes = transcription_regions(ratio_data)    
    lilypond_create(notes,output_file)      
    os.startfile(output_file)

if __name__ == "__main__":
    main()