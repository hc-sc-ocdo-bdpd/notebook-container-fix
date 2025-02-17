# File Processing Library

➜ [**Starter code**](https://github.com/hc-sc-ocdo-bdpd/file_processing_tools_template
)

➜ [**Documentation**](https://hc-sc-ocdo-bdpd.github.io/file-processing-tools/)

## Overview

This library contains tools for processing various file types for several purposes. This includes extracting metadata from files and directories and calculating metrics between files such as cosine similarity and Levenshtein distance. This software is under active development.

## Installation and Dependencies

If starting from scratch, use:

```
pip install git+https://github.com/hc-sc-ocdo-bdpd/file-processing-tools.git
```

Additionally, this project uses tesseract for OCR. This must be installed at: `C:/Users/USERNAME/AppData/Local/Programs/Tesseract-OCR/tesseract.exe`. See https://github.com/UB-Mannheim/tesseract/wiki.

This project also uses ffmpeg for audio/video file transcripting. You can install it via PowerShell using the following steps: 
1. Install scoop: `iwr -useb get.scoop.sh | iex` 
2. Install ffmpeg: `scoop install ffmpeg`
3. It may be necessary to restart the IDE and computer after these installs have been completed
