from django.test import TestCase

from catalog.models import *

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')

# class BookModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         Book.objects.create(title='PooP', summary='1234', isbn='asdf',)

#     def test_title_max_length(self):
#         book = Book.objects.get(id=1)
#         max_length = book._meta.get_field('title').max_length
#         self.assertEquals(max_length, 200)

#     def test_get_absolute_url(self):
#         book = Book.objects.get(id=1)
#         self.assertEquals(book.get_absolute_url(), '/catalog/book/1')
    
#     def test_summary_max_length(self):
#         book = Book.objects.get(id=1)
#         max_length = book._meta.get_field('summary').max_length
#         self.assertEquals(max_length, 1000)
    
#     def test_isbn_max_length(self):
#         book = Book.objects.get(id=1)
#         max_length = book._meta.get_field('isbn').max_length
#         self.assertEquals(max_length, 13)

# class BookInstanceModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         BookInstance.objects.create(imprint='1234', due_back='2020-10-20')
    
#     def test_imprint_max_length(self):
#         bookinstance = BookInstance.objects.get(id=1)
#         max_length = bookinstance._meta.get_field('imprint').max_length
#         self.assertEquals(max_length, 200)
    
#     def test_get_absolute_url(self):
#         bookinstance = BookInstance.objects.get(id=1)
#         self.assertEquals(bookinstance.get_absolute_url(), '/catalog/book/1')