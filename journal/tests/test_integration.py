from datetime import date
from django.test.client import Client, RequestFactory
from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

from journal.views import *


class JournalEntryIntegrationTests(LiveServerTestCase):

	@classmethod
	def setUpClass(cls):
		cls.selenium = WebDriver()
		super(JournalEntryIntegrationTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super(JournalEntryIntegrationTests, cls).tearDownClass()

	def test_journal_entry_listed(self):
		Journal_Entry.objects.create(route='a path', distance_in_kilometers=10)
		self.selenium.get('%s%s' % (self.live_server_url, '/journal/'))
		self.assertEqual(
			self.selenium.find_elements_by_tag_name('li')[0].text,
			'a path 10.0KM ' + str(date.today()) + ' (Edit)'
		)

	def test_add_journal_entry_linked(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/journal/'))
		self.assert_(self.selenium.find_element_by_link_text('Add journal entry'))

	def test_add_journal_entry(self):
		self.selenium.get('%s%s' % (self.live_server_url, '/journal/'))
		self.selenium.find_element_by_link_text('Add journal entry').click()

		self.selenium.find_element_by_id('id_route').send_keys('test')
		self.selenium.find_element_by_id('id_distance_in_kilometers').send_keys('10')
		self.selenium.find_element_by_id('save_journal_entry').click()
		
		self.assertEqual(
			self.selenium.find_elements_by_tag_name('li')[-1].text,
			'test 10.0KM ' + str(date.today()) + ' (Edit)'
		)

	def test_update_journal_entry(self):
		pass

	def test_view_journal_entry_details(self):
		pass

	def test_delete_journal_entry_from_entry_details_view(self):
		pass

	def test_delete_journal_entry_from_edit_entry_view(self):
		pass

	def test_back_to_list_link_works_on_details_page(self):
		pass

	def test_back_to_list_link_works_on_edit_entry_page(self):
		pass

	def test_abort_deletion_link_works_on_delete_page(self):
		pass

