from django.db import models


class Contest( models.Model ):
    name = models.CharField( max_length=200 )
    des = models.TextField()
    img = models.ImageField( upload_to='pics' )
    input = models.TextField()
    output = models.TextField()
    cons = models.TextField()
    discussion = models.TextField()

