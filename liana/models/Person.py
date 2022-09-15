from odoo import api, fields, models


class Person(models.Model):
    _name = 'liana.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')


class Kasir(models.Model):
    _name = 'liana.kasir'
    _inherit = 'liana.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

class Gudang(models.Model):
    _name = 'liana.gudang'
    _inherit = 'liana.person'
    _description = 'New Description'

    id_gudang = fields.Char(string='ID Gudang')

class Kebersihan(models.Model):
    _name = 'liana.kebersihan'
    _inherit = 'liana.person'
    _description = 'New Description'

    id_kebersihan = fields.Char(string='ID Kebersihan')


