Xset.chatter = 10
comp_add = 'atable{' + f'{nlte_file}' + '}'
comp_mult1 = 'TBabs'
comp_mult2 = 'ismabs'
comp_mult3 = 'redden'

mod_2 = f'{comp_mult1}*{comp_mult2}*{comp_mult3}*{comp_add}'

AllModels.clear()
model2 = Model(mod_2)