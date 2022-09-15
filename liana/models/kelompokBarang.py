from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'liana.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('material', 'Material'),
        ('furniture', 'Furniture'),
        ('perlengkapan lainnya', 'Perlengkapan Lainnya')
    ], string='Nama Kelompok')

    kode_kelompok = fields.Char(string='Kode Kelompok')
    
    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'material':
            self.kode_kelompok = 'MAK01'
        elif self.name == 'Furniture':
            self.kode_kelompok = 'MAK02'
        elif self.name == 'Perlengkapan lainnya':
            self.kode_kelompok = 'MIN01'

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='liana.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')
    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')
    
		# Perubahannya di sini
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['liana.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')