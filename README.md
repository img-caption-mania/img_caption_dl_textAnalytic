# img_caption_dl_textAnalytic
img_caption based on deep learning and textAnalytic class at University Islam Indonesia

- after download all images using chrome extension download all image

- create unique name in folder
 
      python script_utils/randomfilerenamer.py 1_tugu_jogja 

- captioning image
- read file  
- python read_file.py <folder_image> <output_readfile>

      python script_utils/read_file.py ../1_tugu_jogja name_file.txt

- mapping anotasi
- python mapping_anotasi.py <list_anotasi manual> <output_readfile> <output caption json>

```bash
python script_utils/mapping_anotasi.py list_anotasi.txt name_file.txt caption_tugu.json
```
  
- manually crosscheck
http://jsonviewer.stack.hu/

- Finally merge all captions and image into each of it's folder
