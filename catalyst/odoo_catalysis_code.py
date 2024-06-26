Odoo code

Stage is set to "New requests"
                if prod.mapped('x_studio_total_freight')[0] > 0:
                    total_qty += prod.mapped('x_studio_total_qty_recd')[0]
        rec['x_studio_qty_wfrt_1'] = total_qty

x_studio_product_category
for rec in self:
  if rec['x_studio_product_category']:
    category = rec['x_studio_product_category'].id
    # search for all prods that have our category_id
    prods_recs = self.env['product.template'].search([('categ_id','=', category)])
    total_frt = 0
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
# CAT-003 create Preliminary Price card in kanban view with oportunity info
if record.name:
    desc="%s-Preliminary Product"%record.name
    card_info ={
        'x_studio_product_name': record.id,
        'x_studio_partner_id': record.partner_id.id,
        'x_studio_user_id': record.user_id.id,
        'x_studio_value': record.expected_revenue,
        'x_studio_kanban_state': 'normal',
        'x_studio_selection_field_1su_1ho8cdkmu': 'create_formula'
    }
    # _logger.info(str(card_info))
    env['x_pricing'].create(card_info)
    #raise UserError(desc+str(card_info))
    
    
Stage is set to "Pricing Approved"
# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}
# CAT-001 create a copy of project template when stage is set to Pricing Approved
# by Jesus Cruz 02.27.2024
if record.name:
    desc="%s-Project"%record.name
    env['project.project'].browse(8).copy({'name': desc})
    prj_s = ''
    l_projects = env['project.project'].search([('name', '=', 'Product Development')])
    #l_projects = env['project.project'].search([]) # all records
    for nproj in env['project.project'].search([('name', '=', 'Product Development')]):
        nproj.unlink()
    #raise UserError("Project list: %s"%(l_projects))
    
https://www.odoo.com/es/forum/ayuda-1/button-to-open-product-record-in-tree-view-84592
tps://www.cybrosys.com/odoo/odoo-books/odoo-book-v15/manufacturing/bills-of-materials/

x_preliminary_quotatio_line_81e9.x_studio_ingredients_list.x_studio_cuanto
x_studio_ingredients_list
x_studio_cuanto
x_studio_cost_

computed_total = 0
#self.env['my.model'].browse([1, 2, 3])
l_prods = self.env['x_preliminary_quotatio_line_81e9'].browse(x_studio_ingredients_list)
for recs in self:
    recs['x_studio_cost_subtotal_1'] = 10
#    computed_total += recs['x_studio_cuanto'] * recs['x_studio_cost_']
#if env['x_preliminary_quotatio']:
#        record['x_studio_cost_subtotal_1'] = 10
#    else:
#        record['x_studio_cost_subtotal_1'] = 100
        
# raw object x_preliminary_quotatio    
self =
{
  "activity_calendar_event_id": false,
  "activity_date_deadline": false,
  "activity_exception_decoration": false,
  "activity_exception_icon": false,
  "activity_ids": [],
  "activity_state": false,
  "activity_summary": false,
  "activity_type_icon": false,
  "activity_type_id": false,
  "activity_user_id": false,
  "create_date": "2024-03-08 10:13:41",
  "create_uid": [
    2,
    "Francisco Estevez"
  ],
  "display_name": "REF004",
  "has_message": true,
  "id": 16,
  "message_attachment_count": 0,
  "message_follower_ids": [],
  "message_has_error": false,
  "message_has_error_counter": 0,
  "message_has_sms_error": false,
  "message_ids": [
    7923,
    7820,
    7819
  ],
  "message_is_follower": false,
  "message_needaction": false,
  "message_needaction_counter": 0,
  "message_partner_ids": [],
  "my_activity_date_deadline": false,
  "rating_ids": [],
  "website_message_ids": [],
  "write_date": "2024-03-19 16:53:11",
  "write_uid": [
    41,
    "Jesus Cruz"
  ],
  "x_active": true,
  "x_color": 0,
  "x_name": "REF004",
  "x_studio_account_manager": [
    37,
    "Jimmy Brashares"
  ],
  "x_studio_bottle_color": false,
  "x_studio_bottle_type": false,
  "x_studio_cost_subtotal_1": 0.7364008166954799,
  "x_studio_cotton": false,
  "x_studio_currency_id": false,
  "x_studio_customer": [
    457,
    "Raw Supplements"
  ],
  "x_studio_customer_tier": "Diamond",
  "x_studio_desiccant": true,
  "x_studio_ingredients_list": [
    131,
    132,
    133,
    134,
    135,
    136,
    137,
    138,
    139,
    140,
    141,
    142,
    143,
    144,
    145,
    146,
    147,
    148,
    149,
    150,
    151,
    152,
    153,
    154,
    155,
    184,
    185
  ],
  "x_studio_kanban_state": false,
  "x_studio_lid_color": false,
  "x_studio_lid_type": false,
  "x_studio_many2many_field_876_1hoeumgks": [
    2224,
    2227
  ],
  "x_studio_neckband": false,
  "x_studio_notes": false,
  "x_studio_one2many_field_7gq_1hoeuk2ik": [],
  "x_studio_one2many_field_8l4_1hoen2j32": [],
  "x_studio_opportunity_name": [
    1992,
    "CBUM Energy Premix"
  ],
  "x_studio_order_quantities_price": [
    3,
    4,
    5
  ],
  "x_studio_packaging": false,
  "x_studio_priority": false,
  "x_studio_priority_1": "0",
  "x_studio_product_type": "Powder",
  "x_studio_quote_is_confirmed": false,
  "x_studio_quote_status": "Draft",
  "x_studio_related_field_5ap_1hoel97es": "Powder",
  "x_studio_scoop": false,
  "x_studio_sequence": 10,
  "x_studio_servings_per_bottle": 0,
  "x_studio_stage_id": [
    2,
    "Create Quotation Formula"
  ],
  "x_studio_total_input_mgserv": 9258.991785158849
}

# Inventory/Product calculation

# x_studio_total_qty_recd = x_studio_qty_recd_wfrt + x_studio_qty_recd_wo_frt_2
x_studio_qty_recd_wfrt, x_studio_qty_recd_wo_frt_2
for rec in self:
  rec['x_studio_total_qty_recd'] = rec['x_studio_qty_recd_wfrt'] + rec['x_studio_qty_recd_wo_frt_2']

# x_studio_total_freight = x_studio_vendor_freight_cost + x_studio_sub_total_freight
x_studio_vendor_freight_cost, x_studio_sub_total_freight
for rec in self:
  rec['x_studio_total_freight'] = rec['x_studio_vendor_freight_cost'] + rec['x_studio_sub_total_freight']

# x_studio_total_unit = x_studio_total_freight / x_studio_total_qty_recd
x_studio_total_freight, x_studio_total_qty_recd
for rec in self:
  rec['x_studio_total_unit'] = 0 if rec['x_studio_total_qty_recd'] == 0 else rec['x_studio_total_freight'] / rec['x_studio_total_qty_recd']

# Preliminary Quote/Configuration/Freight Configuration calculation
x_studio_product_category
# loop for sum
for rec in self:
  if rec['x_studio_product_category']:
    category = rec['x_studio_product_category'].id
    # search for all prods that have our category_id
    prods_recs = self.env['product.template'].search([('categ_id','=', category)])
    total_qty = 0
    if len(prods_recs) > 0:
      for prod in prods_recs:
        if prod.mapped('x_studio_total_freight')[0] > 0:
          total_qty += prod.mapped('x_studio_total_qty_recd')[0]
    rec['x_studio_qty_wfrt_1'] = total_qty
# change
for rec in self:
    if rec['x_studio_product_category']:
        #category = rec['x_studio_product_category'].id
        suffix = rec['x_name']
        # search for all prods that have our category_id
        #prods_recs = self.env['product.template'].search([('categ_id','=', category)])
        prods_recs = self.env['product.template'].search([('x_studio_freight_config_1','=', suffix)])
        total_qty = 0
        if len(prods_recs) > 0:
            for prod in prods_recs:
              if len(prods_recs) > 0:
                for prod in prods_recs:
                  if prod.mapped('x_studio_total_freight')[0] > 0:
                    total_frt += prod.mapped('x_studio_total_freight')[0]
    rec['x_studio_freight'] = total_frt

x_studio_product_category
for rec in self:
  if rec['x_studio_product_category']:
    category = rec['x_studio_product_category'].id
    # search for all prods that have our category_id
    prods_recs = self.env['product.template'].search([('categ_id','=', category)])
    totalwo_frt = 0
    if len(prods_recs) > 0:
      for prod in prods_recs:
        if prod.mapped('x_studio_total_freight')[0] == 0:
          totalwo_frt += prod.mapped('x_studio_total_qty_recd')[0]
    rec['x_studio_qty_wo_frt_1'] = totalwo_frt

x_studio_product_category
for rec in self:
  if rec['x_studio_product_category']:
    category = rec['x_studio_product_category'].id
    # search for all prods that have our category_id
    prods_recs = self.env['product.template'].search([('categ_id','=', category)])
    totalto_frt = 0
    if len(prods_recs) > 0:
      for prod in prods_recs:
        if prod.mapped('x_studio_total_freight')[0] == 0:
          totalto_frt += prod.mapped('x_studio_total_freight')[0]
    rec['x_studio_qty_wo_frt_1'] = totalto_frt

# Preliminary Quote
# Total Input (mg/serv)
# x_studio_total_input_mgserv = sum(x_studio_actual_input)
x_studio_ingredients_list, x_studio_ingredients_list.x_studio_actual_input

for rec in self:
    subtotal = 0
    for line in rec['x_studio_ingredients_list']:
        subtotal += line['x_studio_actual_input']
    rec['x_studio_total_input_mgserv'] = subtotal

# Total Cost (per unit)
# x_studio_total_cost_per_unit = sum(x_studio_cost)
x_studio_ingredients_list, x_studio_ingredients_list.x_studio_cost

for rec in self:
    subtotal = 0
    for line in rec['x_studio_ingredients_list']:
        subtotal += line['x_studio_cost']
    rec['x_studio_total_cost_per_unit'] = subtotal

# Total freight (per unit)
# x_studio_total_freight_per_unit_1 = sum(x_studio_freightunit)
x_studio_ingredients_list, x_studio_ingredients_list.x_studio_freightunit

for rec in self:
    subtotal = 0
    for line in rec['x_studio_ingredients_list']:
        subtotal += line['x_studio_freightunit']
    rec['x_studio_total_freight_per_unit_1'] = subtotal

# Total formula %
# x_studio_total_formula = sum(x_studio_formula_)
x_studio_ingredients_list, x_studio_ingredients_list.x_studio_formula_

for rec in self:
    subtotal = 0
    for line in rec['x_studio_ingredients_list']:
        subtotal += line['x_studio_formula_']
    rec['x_studio_total_formula'] = subtotal
# Preliminary Quote/Ingredients
    
# Formula %
# x_studio_formula_ = x_studio_actual_input / sum(x_preliminary_quotatio.x_studio_total_input_mgserv)
x_studio_actual_input

#preliminary_quotatio_recs = self.env['x_preliminary_quotatio'].search([('x_studio_total_input_mgserv', 'ilike', value)], limit=1)
#mini_rec = self.env['est.weight'].search([])
#mini = mini_rec.mapped('min')
preliminary_quotatio_recs = self.env['x_preliminary_quotatio'].search([])
total_input = preliminary_quotatio_recs.mapped('x_studio_total_input_mgserv')[0]
for record in self:
    record['x_studio_formula_'] = record['x_studio_actual_input']/total_input

# search for product by part number
# x_studio_price = "product.template".standard_price == "Component"? 1000 * "product.template".standard_price : 0
x_studio_part_number, x_studio_cuanto, x_studio_some_name
# price kg
for rec in self:
  if rec['x_studio_part_number']:
    prod_rec = self.env['product.template'].search([('default_code','ilike', rec['x_studio_part_number'])], limit=1)
    prod_categ = prod_rec.mapped('categ_id')[0]
    #rec['x_studio_cuanto'] = prod_categ.id
    #rec['x_studio_text_some'] = prod_categ.complete_name
    #[("categ_id", "ilike", "Component")]
    price_used = 0
    if "Component" in prod_categ.complete_name:
      # use  standard_price /g
      price_used = 1000 * prod_rec.mapped('standard_price')[0]
    rec['x_studio_price'] = price_used

# cost per unit
# in a separate _field x_studio_crm_lead_multine_text
seleccion_rec = self.env['x_preliminary_quotatio'].search([])
seleccion = seleccion_rec.mapped('x_studio_opportunity_name')[0]
for rec in self:
    rec['x_studio_crm_lead_multine_text'] = str(seleccion.id)

x_studio_actual_input, x_studio_price
#x_studio_text_some, x_studio_cuanto
# x_studio_cost = (x_studio_actual_input/1000000)*x_studio_price*'crm.lead'.x_studio_serves_per_bottlebag_bags_2
# serving per bottle, input_mg_serv, price_kg
# lets get opportunity name and get serves_per_bottle
# widget must be selection
selection_rec = self.env['x_preliminary_quotatio'].search([])
selection = selection_rec.mapped('x_studio_opportunity_name')[0]
for rec in self:
    #rec['x_studio_cuanto'] = seleccion.id
    rec_lead_crm = self.env['crm.lead'].search([('id', '=', selection.id)], limit=1)
    #rec['x_studio_cuanto'] = rec_lead_crm.mapped('x_studio_serves_per_bottlebag_bags_2')[0]
    serves_per_bottle = rec_lead_crm.mapped('x_studio_serves_per_bottlebag_bags_2')[0]
    rec['x_studio_cost'] = (rec['x_studio_actual_input']/1000000) * rec['x_studio_price'] * serves_per_bottle

crm.lead
x_preliminary_quotatio.x_studio_opportunity_name

#seleccion = self._fields['x_studio_opportunity_name'].selection  
seleccion = self._fields['x_studio_opportunity_name']
for rec in self:
    rec['x_studio_selection_crmlead'] = seleccion

# freight per kg
# x_studio_freightkg = "crm.lead".x_studio_freight_value_selected" > 0? "crm.lead".x_studio_unit_total : x_studio_price * crm.lead".x_studio_freight_value_selected"
x_studio_text_some, x_studio_price, x_studio_part_number, x_studio_product_category

# get oportunity id and then freight field
selection_rec = self.env['x_preliminary_quotatio'].search([])
selection = selection_rec.mapped('x_studio_opportunity_name')[0]
# get badge
rec_lead_crm = self.env['crm.lead'].search([('id', '=', selection.id)], limit=1)
freight = rec_lead_crm.mapped('x_studio_freight_1')
# get value selected
freight_val = rec_lead_crm.mapped('x_studio_freight_value_selected')
for rec in self:
    # get product category
    prod_rec = self.env['product.template'].search([('default_code','ilike', rec['x_studio_part_number'])], limit=1)
    prod_categ_id = prod_rec.mapped('categ_id')[0]
    #rec['x_studio_text_some'] = str(freight[0])
    if freight_val > 0:
      # look for category_id in Freight Config Table
      freight_rec = self.env['x_freight_configuratio'].search([('x_studio_product_category.id', '=', prod_categ_id)])[0]
      freight_unit_total = freight_rec.mapped('x_studio_unit_total')
      rec['x_studio_freightkg'] = freight_unit_total
    else:
      rec['x_studio_freightkg'] = rec['x_studio_price'] * freight_val

# freight per unit
# x_studio_freightunit = (x_studio_actual_input/1000000) * x_studio_freightkg * "crm.lead"."x_studio_serves_per_bottlebag_bags_2
x_studio_actual_input, x_studio_freightkg

# widget must be selection
selection_rec = self.env['x_preliminary_quotatio'].search([])
selection = selection_rec.mapped('x_studio_opportunity_name')[0]
rec_lead_crm = self.env['crm.lead'].search([('id', '=', selection.id)], limit=1)
serves_per_bottle = rec_lead_crm.mapped('x_studio_serves_per_bottlebag_bags_2')[0]
for rec in self:
  rec['x_studio_freightunit'] = (rec['x_studio_actual_input'] / 1000000) * rec['x_studio_freightkg'] * serves_per_bottle

# cost %
# x_studio_cost_ = x_studio_cost / sum(x_preliminary_quotatio.x_studio_total_cost_per_unit)
x_studio_cost

preliminary_quotatio_recs = self.env['x_preliminary_quotatio'].search([])
total_cost = preliminary_quotatio_recs.mapped('x_studio_total_cost_per_unit')[0]
for record in self:
    if total_cost > 0:
        record['x_studio_cost_'] = record['x_studio_cost']/total_cost
    else:
        record['x_studio_cost_'] = 0