# musicRR

An alternative representation of RR peak data in terms of musical notation.

**On the MacOS version window resizing is disabled**

For the windows version please go to: https://github.com/msharr/Visualising-RR-Through-Music

## Prerequisites

Latest version of python installed.

Download Lilypond from https://lilypond.org/download.html and make sure that the default program for running `.ly` files is set to Lilypond.

> Depending on the version of macOS and Lilypond the main download link may not work. In this case try the alternatives suggested on the download page

## Running the program

Download the files in the repository.

Open the terminal app and navigate to where the program files have been downloaded. By default this should be:

```bash
cd downloads
cd Visualising-RR-Through-Music-MacOS-master
```

Next install the dependencies by running in the terminal:

```bash
pip3 install -r requirements.txt
```

or

```bash
pip install -r requirements.txt
```

Once the dependencies have been installed, the program is ready to run. Close the terminal and navigate to the project folder. Run `GUI.py`

Enter the parameters:

`Time` - Format is HH:mm (24 hour time)

`Date` - Format is dd/mm/yyyy

`Tuning Level` - Maximum percentage difference between the BPM of two bars before they are categorised differently. Value is between 0 - 1

`Exclusion Duration` - Excludes bars below value in seconds. Off by default as useful information may be excluded - use with caution.

`Min Tempo` & `Max Tempo` - Min Tempo < x < Max Tempo, heart rates (BPMs) below min tempo and above max tempo are excluded.

Next you must select the data by clicking the `Patients` button. Please select an appropriate `.txt` file, example shown below.

## Data format

Place data in a **text file** in the same format as below. Length is capped at 15000 due to a limitation with Lilypond.

```
656
727
688
688
648
773
695
625
672
687
633
688
711
726
586
672
680
711
695
672
687
```
