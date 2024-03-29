# 🧜 Caliban

A very simple python app to detect the genre of an audio file using a Mel Spectogram and a simple CNN with PyTorch.

Currently we're trained with just 10 Geners using the GTZAN data set, but working to retrain on the Million Songs dataset for a wider array of results and geners. As shown here http://millionsongdataset.com/sites/default/files/AdditionalFiles/unique_terms.txt

## Usage
```
$ docker-compose up -d application
```

Then just send it a file.
```
curl --request POST \
  --url http://127.0.0.1:5000/ \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form file=/path/to/file
```

[Million Songs](https://aws.amazon.com/datasets/million-song-dataset/)
[GTZAN Genre Collection](http://marsyas.info/downloads/datasets.html) 

## Thanks
Big thanks for [cetinsame](https://github.com/cetinsame) for the work on the original model.
