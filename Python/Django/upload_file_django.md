# Upload files with Django

##Links
* https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
* https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/
* https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example

# Front-end
```html
<div class="container">
    <form class="form-horizontal" method="POST" enctype="multipart/form-data" action="/submit_request">
        {% csrf_token %}

	<!-- input element for upload -->
    </form>
</div>
```

# Back-end
## Upload any file and save to db
```python
agreement_file = request.FILES["agreement_uploaded"]
fs = FileSystemStorage()
filename = fs.save(agreement_file.name, agreement_file)
agreement_uploaded_url = fs.url(filename)

## get the file content
agreement_uploaded_fullpath = os.path.join(fs.location, filename)

with open(agreement_uploaded_fullpath, 'rb') as f:
    pdf_encoded = base64.b64encode(f.read())
```


## Get the content from uploaded file
```python
agreement_file = request.FILES["agreement_uploaded"]
agreement_file_content = agreement_file.read()
```


## Save uploaded file to filesystem
```python
agreement_file = request.FILES["agreement_uploaded"]
fs = FileSystemStorage()
filename = fs.save(agreement_file.name, agreement_file)
agreement_uploaded_url = fs.url(filename)

# get the file content
agreement_uploaded_fullpath = os.path.join(fs.location, filename)
```

## Retrieve file from db and save to filesystem
```python
file = Requests.objects.values_list('agreement_uploaded').filter(id=1)[0][0]
pdf_enc = base64.b64decode(file)
with open('test.pdf', 'wb') as write_pdf_test:
    write_pdf_test.write(pdf_enc)
```


### Full Explanation
```python
def uploadView(request):
    upFile = request.FILES["upFile"]
```

where upFile is an UploadedFile object, which is not a file-like object. An UploadedFile has the following properties:

* ```name```: name of the uploaded file
* ```size```: size in bytes

and the following methods:

* ```read()```: Read the entire file and return as a string. Probably good for you, but not recommended for files over 2.5 MB.
* ```multiple_chunks()```: Returns True if the file should be handled as multiple chunks.
* ```chunks()```: Returns a generator (use it like an iterator) which returns the file data one chunk at a time.

So, continuing the example, if you just wanted to save the file to disk, you could write:

```python
outFile = open("/tmp/uploadTest.txt", "w")
if not upFile.multiple_chunks():
    outFile.write(upFile.read())
else:
    for chunk in upFile.chunks():
        outFile.write(chunk)
outFile.close()
```

You could probably just show an error message and discard the file if ```multiple_chunks()``` returns ```True```, since you probably aren't looking to put over 2.5 MB of text on your page.


Assuming the file isn't over 2.5 MB, your view function could look like:
```python
def uploadView(request):
    upFile = request.FILES["upFile"]
    context = {}
    if upFile.multiple_chunks():
        context["uploadError"] = "Uploaded file is too big (%.2f MB)." % (upFile.size,)
    else:
        context["uploadedFile"] = upFile.read()
    return render_to_response('fileUploadPage.html', context)
```
