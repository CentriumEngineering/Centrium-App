from Range_Conversion import Range_Conversion
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Forms import Range_Form

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# all Flask routes below


@app.route("/", methods=["GET", "POST"])
def home():
    scaled_values = [0, 0, 0]
    range_data_float = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    form = Range_Form(pv1_val=0, pv2_val=0, pv3_val=0, pv1_min=4, pv2_min=0, pv3_min=0, pv1_max=20, pv2_max=100,
                      pv3_max=100)  # default values

    if request.method == 'POST':
        data = request.form.to_dict()
        keys_to_delete = ['loop', 'pv1_val', 'pv1_unit', 'pv2_val', 'pv2_unit', 'pv3_val', 'pv3_unit', 'submit']
        range_data = {x: y for x, y in data.items() if x not in keys_to_delete}
        range_data_float = [float(x) for x in range_data.values()]
        if data['pv_select'] == '0':
            range_data_float.insert(6, float(data['pv2_val']))
        elif data['pv_select'] == '1':
            range_data_float.insert(6, float(data['pv1_val']))
        else:
            range_data_float.insert(6, float(data['pv3_val']))

        scaled_values = Range_Conversion(*range_data_float)

    return render_template("index.html", form=form, pv1_val=scaled_values[0], pv2_val=scaled_values[1],
                           pv3_val=scaled_values[2], pv1_range=range_data_float[1] - range_data_float[0],
                           pv1_min=range_data_float[0], pv2_range=range_data_float[3] - range_data_float[2],
                           pv2_min=range_data_float[2], pv3_range=range_data_float[5] - range_data_float[4],
                           pv3_min=range_data_float[4])


if __name__ == '__main__':
    app.run(debug=True)

    # print(Range_Conversion(-10, 15, 0, 100, -5, 15, 85, 0))
    # print(Range_Conversion(-10, 15, 0, 100, -5, 15, 11.25, 1))
    # print(Range_Conversion(-10, 15, 0, 100, -5, 15, 12, 2))

    # print(Range_Conversion(4, 20, 0, 100, 0, 3000, 25, 0))
    # print(Range_Conversion(4, 20, 0, 100, 0, 3000, 8, 1))
    # print(Range_Conversion(4, 20, 0, 100, 0, 3000, 750, 2))
