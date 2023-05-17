# Categorise bars
def categorisation(ratio, tuning_level):
    category = []
    category.append(ratio[0])
    for i in range(1,len(ratio)-1):
        if ratio[i].notes == category[len(category)-1].notes:
            if (int(category[len(category)-1].tempo * (1-tuning_level))) <= ratio[i].tempo <= int((category[len(category)-1].tempo * (1+tuning_level))):
                category[len(category)-1].end = ratio[i].end
            else:
                category.append(ratio[i])
        else:
            category.append(ratio[i]) 
    return category

def categorisation2(ratio, tuning_level,exclusion_level):
    category = []
    category.append(ratio[0])
    for i in range(1,len(ratio)-1):
        if ratio[i].notes == category[len(category)-1].notes:
            if (int(category[len(category)-1].tempo * (1-tuning_level))) <= ratio[i].tempo <= int((category[len(category)-1].tempo * (1+tuning_level))):
                category[len(category)-1].end = ratio[i].end
            else:
                if category[len(category)-1].end - category[len(category)-1].start < exclusion_level:
                    del category[len(category)-1]
                category.append(ratio[i])
        else:
            if category[len(category)-1].end - category[len(category)-1].start < exclusion_level:
                del category[len(category)-1]
            category.append(ratio[i]) 
    return category

def tempo_exclusion(ratio, min_tempo, max_tempo):
    included = []
    for i in range(len(ratio)-1):
        if  min_tempo < ratio[i].tempo < max_tempo :
            included.append(ratio[i])
    return included

def main(patient_bars, tuning_level, exclusion_level, min_tempo, max_tempo):
    categorised_data = categorisation(patient_bars, tuning_level)
    categorised_data = tempo_exclusion(categorised_data, min_tempo, max_tempo)
    categorised_data = categorisation2(categorised_data, tuning_level,exclusion_level)
    categorised_data = categorisation2(categorised_data, tuning_level,exclusion_level)
    # categorised_data = categorisation(categorised_data, tuning_level)
    return categorised_data

if __name__ == "__main__":
    main()