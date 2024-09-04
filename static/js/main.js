new Vue({
    el: '#app',
    data: {
        currentView: 'home'
    },
    components: {
        home: {
            template: '<div>Home Component</div>'
        },
        about: {
            template: '<div>About Component</div>'
        }
    },
    methods: {
        navigate(view) {
            this.currentView = view;
        }
    }
});

function comprobarCedula() {
    let user_cedula = document.getElementById('user_cedula').value;

    obtenerDatosEstudiante(user_cedula)
        .then(respuesta => {
            console.log(respuesta);

            if (respuesta.length === 0) {
                alert('Esta cédula no existe en el sistema, por favor comprueba los datos');
                return;
            } else {
                let estudiante = respuesta[0];
                let idEstudiante = estudiante.id;
                let str = estudiante.lastname;
                let parts = str.split(' ');

                console.log(parts);
                document.getElementById('user_nombres').value = estudiante.firstname;
                document.getElementById('user_apellido_p').value = parts[0];
                document.getElementById('user_apellido_m').value = parts[1];
                document.getElementById('user_correo').value = estudiante.email;
                document.getElementById('user_telefono_Movil').value = estudiante.customfields[4].value;
                datosComprobados = true;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function obtenerDatosEstudiante(cedula) {
    console.log(cedula);
    return fetch(`https://cursos.isteps.edu.ec/webservice/rest/server.php?wstoken=33b23cd3fa1ae0d0e5d3d4df15541222&wsfunction=core_user_get_users_by_field&field=username&values[0]=${cedula}&moodlewsrestformat=json`)
        .then(response => response.json());
}
