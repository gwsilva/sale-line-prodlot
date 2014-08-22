# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Gideoni Silva (Omnes)
#    Copyright 2013-2014 Omnes Tecnologia
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import orm, osv, fields

class sale_order(orm.Model):
    _inherit = 'sale.order'

    def action_wait(self, cr, uid, ids, context=None):
        """
        In sale order:
            - the prodlot must be fill before confirm sale order
        """
        context = context or {}

        for o in self.browse(cr, uid, ids):
                for l in o.order_line:
                    if not l.prodlot_id:
                        raise orm.except_orm(
                            _('Lote do Produto não informado !'), 
                            _('Por favor, informar o lote para o produto : %s') % (l.product_id.name))
                            
        return super(sale_order, self).action_wait(cr, uid, ids, context=context)
        

    def _prepare_order_line_move(self, cr, uid, order, line, picking_id, date_planned, context=None):
        """
        Envia o prodlot_id presente no sale_order_line para o stock_move
        """
        results = super(sale_order, self)._prepare_order_line_move(cr, uid, order=order, line=line, picking_id=picking_id, date_planned=date_planned, context=context)
        if l.prodlot_id:
                results['prodlot_id'] = l.prodlot_id.id
        return results



class sale_order_line(osv.osv):
    _inherit = 'sale.order.line'

    _columns = {
        'prodlot_id': fields.many2one('stock.production.lot', 'Production Lot', domain="[('product_id','=',product_id)]", readonly=True, states={'draft': [('readonly', False)]}, help='Production lot is used to put a serial number on the production'),
     }
#"""
#def _get_prodlot_context(self, cr, uid, context=None):
#        context = context or {}
#        shop_id = context.get('shop', False)
#        shop_obj = self.pool.get('sale.shop')
#        shop = shop_obj.browse(cr, uid, shop_id)
#        prodlot_context = {}
#        if(not shop_id):
#            return {}
#        if shop:
#            location_id = shop.warehouse_id and shop.warehouse_id.lot_stock_id.id
#            if location_id:
#                prodlot_context['location_id'] = location_id
#        return prodlot_context
#
#
#def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
#                          uom=False, qty_uos=0, uos=False, name='', partner_id=False, 
#                          lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, 
#                          flag=False, context=None, **kwargs):
#        context = context or {}
#
#
#        warning_msgs = ''
#            
#        product_obj = product_obj.browse(cr, uid, product, context=context_partner)
#        stock_prod_lot = self.pool.get('stock.production.lot')
#        
#        for prodlot_id in stock_prod_lot.search(cr, uid,[('product_id','=',product_obj.id)]):
#            prodlot_context = self._get_prodlot_context(cr, uid, context=context)
#            prodlot = stock_prod_lot.browse(cr, uid, prodlot_id, context=prodlot_context)
#"""
#
#
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
