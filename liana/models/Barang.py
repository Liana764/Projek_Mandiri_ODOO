# from odoo import api, fields, models
from odoo import fields, models


class Barang(models.Model):
    _name = 'liana.barang'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    # Comodel adalah menentukkan model mana yang menjadi one-nya
    kelompokbarang_id = fields.Many2one(comodel_name='liana.kelompokbarang',
                                        string='Kelompok Barang',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(
        comodel_name='liana.supplier',
        string='Supplier')
		# Perubahannya di sini
    stok = fields.Integer(string='Stok')