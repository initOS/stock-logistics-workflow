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
from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _compute_progress(self):
        for picking in self:
            ok = map(
                lambda sm: 1 if sm.state == 'done' else 0,
                [ml for ml in picking.move_lines if ml.state != 'cancel']
            )
            num, denom = sum(ok), len(ok)
            picking.progress = (num * 100.0) / denom if denom > 0 else 100.0

    progress = fields.Float(
        string='Progress',
        compute='_compute_progress',
        store=False,
        help="Percentage of non-cancelled stock moves that are done.",
    )
