# -*- coding: utf-8 -*-
# © 2018 initOS GmbH (<http://www.initos.com>)
# Author: Mathias Francke <mathias.francke at initos.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openerp import SUPERUSER_ID
from openerp.api import Environment

import logging

_logger = logging.getLogger(__name__)

def pre_init_hook(cr, pool):
    """
    Creates columns for sequence and sequence2 and fills them automatically to
    speed up installation process in populated database.
    """
    _logger.info('Adding sequence and sequence2 to stock_move...')
    cmd = """
        ALTER TABLE stock_move 
         ADD COLUMN sequence  integer,
         ADD COLUMN sequence2 integer;
        """
    cr.execute(cmd)

    _logger.info('Filling sequence of stock_move with initial value (9999)...')
    cmd = """
        UPDATE stock_move 
           SET sequence = 9999;
        """
    cr.execute(cmd)

    _logger.info('Filling sequence2 of stock_move with initial value (9999)...')
    cmd = """
        UPDATE stock_move 
           SET sequence2 = 9999;
        """
    cr.execute(cmd)

    # env = Environment(cr, SUPERUSER_ID, {})
    # stock = env['stock.picking'].search([])
    # stock._reset_sequence()
