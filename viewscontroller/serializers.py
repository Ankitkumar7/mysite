from rest_framework import serializers
from rest_framework import serializers
from .models import Stock, Post
from .models import dayOne, dayTwo, dayThree, dayFour, dayFive, daySix, music,shareYourWeight

class StockSerializerOne(serializers.ModelSerializer):

	class Meta:
		model = dayOne
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerTwo(serializers.ModelSerializer):

	class Meta:
		model = dayTwo
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerThree(serializers.ModelSerializer):

	class Meta:
		model = dayThree
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerFour(serializers.ModelSerializer):

	class Meta:
		model = dayFour
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerFive(serializers.ModelSerializer):

	class Meta:
		model = dayFive
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerSix(serializers.ModelSerializer):

	class Meta:
		model = daySix
		# fields = ('ticker's, 'volume')
		fields = '__all__'

class StockSerializerMusic(serializers.ModelSerializer):

	class Meta:
		model = music
		# fields = ('ticker's, 'volume')
		fields = '__all__'
class AddUserWeightSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		# fields = ('ticker's, 'volume')
		fields = [
			'name',
			'age',
			'weight'
		]

