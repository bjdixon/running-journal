from datetime import date
from django.test.client import Client, RequestFactory
from django.test import TestCase, LiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver

from journal.views import *
from journal.tests.utils import create_journal_entry


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
		self.selenium.get('%s%s' % (self.live_server_url, reverse('journal_entry_list')))
		self.assertEqual(
			self.selenium.find_elements_by_tag_name('li')[0].text,
			'a path 10.0KM ' + str(date.today()) + ' (Edit)'
		)

	def test_add_journal_entry_linked(self):
		self.selenium.get('%s%s' % (self.live_server_url, reverse('journal_entry_list')))
		self.assert_(self.selenium.find_element_by_link_text('Add journal entry'))

	def test_add_journal_entry(self):
		self.selenium.get('%s%s' % (self.live_server_url, reverse('journal_entry_list')))
		self.selenium.find_element_by_link_text('Add journal entry').click()

		self.selenium.find_element_by_id('id_route').send_keys('test')
		self.selenium.find_element_by_id('id_distance_in_kilometers').send_keys('10')
		self.selenium.find_element_by_id('save_journal_entry').click()
		
		self.assertEqual(
			self.selenium.find_elements_by_tag_name('li')[-1].text,
			'test 10.0KM ' + str(date.today()) + ' (Edit)'
		)

	def test_update_journal_entry(self):
		create_journal_entry()
		self.selenium.get('%s%s' % (self.live_server_url, reverse('journal_entry_list')))
		self.selenium.find_element_by_link_text('Edit').click()
		self.selenium.find_element_by_id('id_route').send_keys(' 66')
		self.selenium.find_element_by_id('save_journal_entry').click()

		self.assertEqual(
			self.selenium.find_elements_by_tag_name('li')[-1].text,
			'route 66 10.0KM ' + str(date.today()) + ' (Edit)'
		)

	def test_view_journal_entry_details(self):
		create_journal_entry()
		self.selenium.get('%s%s' % (self.live_server_url, reverse('journal_entry_list')))
		self.selenium.find_element_by_link_text('route 10.0KM ' + str(date.today())).click()
		h2 = self.selenium.find_element_by_tag_name('h2').text
		paragraph = self.selenium.find_element_by_tag_name('p').text
		self.assertEqual(
			h2,
			'route (' + date.today().strftime("%B %d, %Y")  + ')'
		)
		self.assertEqual(
			paragraph,
			'Distance: 10.0KM\nTime:'
		)

	def test_delete_journal_entry_from_entry_details_view(self):
		create_journal_entry()
		self.selenium.get(
			'%s%s' % (
				self.live_server_url, 
				reverse('journal_entry_detail', kwargs={'pk': 1})
			)
		)
		self.selenium.find_element_by_link_text('Delete').click()
		self.selenium.find_element_by_id('journal_entry_delete').click()
		self.assertEqual(Journal_Entry.objects.all().count(), 0)

	def test_delete_journal_entry_from_edit_entry_view(self):
		create_journal_entry()
		self.selenium.get(
			'%s%s' % (
				self.live_server_url, 
				reverse('journal_entry_edit', kwargs={'pk': 1})
			)
		)
		self.selenium.find_element_by_link_text('Delete').click()
		self.selenium.find_element_by_id('journal_entry_delete').click()
		self.assertEqual(Journal_Entry.objects.all().count(), 0)

	def test_back_to_list_link_works_on_details_page(self):
		create_journal_entry()
		self.selenium.get(
			'%s%s' % (
				self.live_server_url,
				reverse('journal_entry_detail', kwargs={'pk': 1})
			)
		)
		self.selenium.find_element_by_link_text('Back to list').click()
		self.assertEqual(
			self.selenium.current_url,
			self.live_server_url + reverse('journal_entry_list')
		)

	def test_back_to_list_link_works_on_edit_entry_page(self):
		create_journal_entry()
		self.selenium.get(
			'%s%s' % (
				self.live_server_url,
				reverse('journal_entry_edit', kwargs={'pk': 1})
			)
		)
		self.selenium.find_element_by_link_text('Back to list').click()
		self.assertEqual(
			self.selenium.current_url,
			self.live_server_url + reverse('journal_entry_list')
		)

	def test_abort_deletion_link_works_on_delete_page(self):
		create_journal_entry()
		self.selenium.get(
			'%s%s' % (
				self.live_server_url,
				reverse('journal_entry_delete', kwargs={'pk': 1})
			)
		)
		self.selenium.find_element_by_link_text('No, Abort!').click()
		self.assertEqual(
			self.selenium.current_url, 
			self.live_server_url + reverse('journal_entry_list')
		)

