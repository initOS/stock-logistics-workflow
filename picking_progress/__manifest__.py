# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2017 initOS GmbH (<http://www.initos.com>).
#    Author: Andreas Zöllner <andreas.zoellner at initos.com>
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
    'name': 'Picking Progress',
    'version': '10.0.1',
    'author': 'initOS GmbH, Odoo Community Association (OCA)',
    'website': 'https://initos.com',
    'license': 'AGPL-3',
    'depends': [
        'stock',
    ],
    'data': [
        'views/stock.xml',
    ],
    'description': """
Picking Progress
================

This module adds a display of the progress of pickings.

The progress of a picking is the percentage of its non-cancelled lines (i.e.,
stock moves) that are 'done'.  It will be displayed as a progress bar in both
the picking tree view and form view.

Contributors
------------
* Andreas Zöllner <andreas.zoellner@initos.com>
    """,
    'installable': True,
    'auto_install': False,
}
