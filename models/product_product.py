from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

class ProductProduct(models.Model):
    _inherit = 'product.product'

    uom_id = fields.Many2one('uom.uom', string='Unit of Measure',default=lambda self: self._get_uom())

    base_uom_category_id = fields.Many2one(
        'uom.category',
        string='UoM Category',
        related='product_tmpl_id.uom_id.category_id',
        readonly=True
    )

    def _get_uom(self):
        """
        Return the UoM for the product variant if defined,
        otherwise fallback to the product template UoM.
        """
        return self.uom_id or self.product_tmpl_id.uom_id
