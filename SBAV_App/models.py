from django.db import models


class Items(models.Model):
	Item_Name = models.CharField(max_length=100, null=True)
	Items_In_Stock = models.IntegerField(blank=True,null=True, default=0)
	Items_Out_Stock = models.IntegerField(blank=True,null=True, default=0)
	Item_Cost = models.IntegerField(blank=True,null=True, default=0)
	Created_at = models.DateTimeField(auto_now_add=True, blank=True)
	
	def __str__(self):
		return "%s" %(self.Item_Name)