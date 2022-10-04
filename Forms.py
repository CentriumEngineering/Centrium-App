from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, url


class Range_Form(FlaskForm):
    loop = StringField('Loop:')
    pv1_val = DecimalField('PV-1 value', places=0)
    pv1_min = DecimalField('PV-1 min value', places=0)
    pv1_max = DecimalField('PV-1 max value', places=0)
    pv1_unit = SelectField(u'Engineering Unit', choices=['mA', '%', 'Psi', 'Deg F/C', 'count', 'none'],
                           validators=[DataRequired()])
    pv2_val = DecimalField('PV-2 value', places=0)
    pv2_min = DecimalField('PV-2 min value', places=0)
    pv2_max = DecimalField('PV-2 max value', places=0)
    pv2_unit = SelectField(u'Engineering Unit', choices=['mA', '%', 'Psi', 'Deg F/C', 'count', 'none'],
                           validators=[DataRequired()])
    pv3_val = DecimalField('PV-3 value', places=0)
    pv3_min = DecimalField('PV-3 min value', places=0)
    pv3_max = DecimalField('PV-3 max value', places=0)
    pv3_unit = SelectField(u'Engineering Unit', choices=['mA', '%', 'Psi', 'Deg F/C', 'count', 'none'],
                           validators=[DataRequired()])

    pv_select = SelectField(u'Calculate',
                            choices=[(0, 'Input PV2'), (1, 'Input PV1'),
                                     (2, 'Input PV3')],
                            validators=[DataRequired()])

    submit = SubmitField('Submit')
