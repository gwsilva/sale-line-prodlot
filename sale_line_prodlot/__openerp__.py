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

{
    'name': 'Serial Number Sale Order Lines',
    'summary': 'Sales Orders',
    'description': 'Serial Number on Sales Orders Lines',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'author': 'Omnes Tecnolgia',
    'website': 'http://www.omnes.net.br',
    'version': '0.1',
    'depends': ['sale', 'stock'],
    'data': ['sale_order_line_extension.xml'],    
    'demo': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
