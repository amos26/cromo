from django.db import models

# Create your models here.

class Pacote(models.Model):
	quantidade = models.IntegerField()
	preco = models.FloatField()

	def __unicode__(self):
		return self.

class Jogador(User):
	endereco = models.CharField(max_length = 255)
	bairro = models.CharField(max_length = 255)
	cidade = models.CharField(max_length = 255)
	cep = models.CharField(max_length = 255)
	amigo = models.ForeignKey( 'self', null = True, blank = True, related_name = 'Amigos' )
	pacote = models.ManyToManyField(Pacote, through = "Compra")

	def __unicode__(self):
		return self.get_full_name()

class Album(models.Model):
	titulo = models.CharField(max_length = 255)
	data_lancamento = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.titulo

class Categoria(models.Model):
	nome = models.CharField(max_length = 40)
	album = models.ForeignKey(Album, related_name = "Categoria do album")
	figura = models.ForeignKey(Album, related_name = "Categoria da figura")

	def __unicode__(self):
		return self.nome

class Figura(models.Model):
	numero = models.IntegerField()
	descricao = models.CharField(max_length = 255)
	fundo = models.FileField(upload_to = "imagem_fundo/")

	def __unicode__(self):
		return self.numero