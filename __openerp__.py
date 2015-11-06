###
#
#   This file is part of odoo-addons.
#
#   odoo-addons is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   odoo-addons is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##

{
    'name': 'Ocultar Opciones en Vistas',
    'author': 'Aristobulo Meneses',
    'version': '0.2',
    'description': '''
Este modulo permite ocultar algunas opciones de la Pestaña <<< Mas >>>
======================================================================

Para Ocultar el boton Duplicar:

En la definicion de la vista formulario o arbil definir un atributo:
    - duplicate="false" 

Ejemplo:

<form string="Users" duplicate="false">
<tree string="Users" duplicate="false">

Para Ocultar el boton Borrar:

En la definicion de la vista formulario o arbil definir un atributo:
    - delete="false" 

<form string="Users" delete="false">
<tree string="Users" delete="false">

    ''',
    'category': 'web',
    'depends': ['web', ],
    'data': ['views/hide_duplicate.xml', ],
    'installable': True,
    'auto_install': False,
    'web': True,
}
