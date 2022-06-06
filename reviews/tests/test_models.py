from django.test import TestCase
from reviews.models import Book, Publisher, Contributor


class TestBookModel(TestCase):
	def test_create_publisher(self):
		publisher = Publisher.objects.create(name="Packt", website="www.packt.com", email="contact@packt.com")
		self.assertIsInstance(publisher, Publisher)


class TestContributorModel(TestCase):
	def test_create_contributor(self):
		contributor = Contributor.objects.create(first_names="Barry", last_names="Allen", email="barry@theflash.com")
		self.assertIsInstance(contributor, Contributor)


class TestBookModel(TestCase):
	def setUp(self):
		self.publisher = Publisher.objects.create(name="Packt", website="www.packt.com", email="contact@packt.com")
		self.contributor = Contributor.objects.create(first_names="Barry", last_names="Allen", email="barry@theflash.com")

	def test_create_book(self):
		book = Book.objects.create(title="The Adventures of The Flash", isbn='1111-00-111', publication_date='2022-04-09', publisher=self.publisher)
		book.contributors.set([self.contributor])
		self.assertIsInstance(book, Book)
