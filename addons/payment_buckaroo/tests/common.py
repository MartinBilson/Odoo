# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.payment.tests.common import PaymentCommon


class BuckarooCommon(PaymentCommon):

    SYNC_NOTIFICATION_DATA = {
        'brq_payment': 'ABCDEF0123456789ABCDEF0123456789',
        'brq_payment_method': 'paypal',
        'brq_statuscode': '190',  # confirmed
        'brq_statusmessage': 'Transaction successfully processed',
        'brq_invoicenumber': 'Test Transaction',  # Shamefully copy-pasted from payment
        'brq_amount': '1111.11',
        'brq_currency': 'USD',
        'brq_timestamp': '2022-01-01 12:00:00',
        'brq_transactions': '0123456789ABCDEF0123456789ABCDEF',
        'brq_signature': '5d389aa4f563cd99666a2e6bef79da3d4a32eb50',
    }

    @classmethod
    def setUpClass(cls, chart_template_ref=None):
        super().setUpClass(chart_template_ref=chart_template_ref)

        cls.buckaroo = cls._prepare_acquirer('buckaroo', update_values={
            'buckaroo_website_key': 'dummy',
            'buckaroo_secret_key': 'test_key_123',
        })

        # Override defaults
        cls.acquirer = cls.buckaroo
        cls.currency = cls.currency_euro
