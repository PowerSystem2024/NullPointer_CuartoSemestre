class Personaje {
    constructor(nombre, vidas = 3) {
        this.nombre = nombre;
        this.vidas = vidas;
        this.ataqueActual = null;
    }

    recibirDano() {
        this.vidas--;
    }

    estaVivo() {
        return this.vidas > 0;
    }

    resetear() {
        this.vidas = 3;
        this.ataqueActual = null;
    }
}

class Ataque {
    constructor(nombre, debilContra = null) {
        this.nombre = nombre;
        this.debilContra = debilContra;
    }

    venceA(otroAtaque) {
        return this.debilContra === otroAtaque.nombre;
    }
}

class Juego {
    constructor() {
        this.jugador = null;
        this.enemigo = null;
        this.ataques = this.inicializarAtaques();
        this.personajes = this.inicializarPersonajes();
        this.interfaz = new Interfaz();
    }

    inicializarAtaques() {
        return {
            'Punio': new Ataque('Punio', 'Barrida'),
            'Patada': new Ataque('Patada', 'Punio'),
            'Barrida': new Ataque('Barrida', 'Patada')
        };
    }

    inicializarPersonajes() {
        return ['Zuko', 'Katara', 'Aang', 'Toph', 'Suki', 'Iroh'];
    }

    seleccionarPersonajeJugador(nombrePersonaje) {
        this.jugador = new Personaje(nombrePersonaje);
        this.seleccionarPersonajeEnemigo();
        this.interfaz.mostrarSeleccionAtaque();
    }

    seleccionarPersonajeEnemigo() {
        const indiceAleatorio = this.aleatorio(0, this.personajes.length - 1);
        const nombreEnemigo = this.personajes[indiceAleatorio];
        this.enemigo = new Personaje(nombreEnemigo);
        this.interfaz.mostrarPersonajes(this.jugador.nombre, this.enemigo.nombre);
    }

    realizarAtaque(nombreAtaque) {
        this.jugador.ataqueActual = this.ataques[nombreAtaque];
        this.ataqueAleatorioEnemigo();
        this.combate();
    }

    ataqueAleatorioEnemigo() {
        const ataquesDisponibles = Object.keys(this.ataques);
        const indiceAleatorio = this.aleatorio(0, ataquesDisponibles.length - 1);
        const nombreAtaque = ataquesDisponibles[indiceAleatorio];
        this.enemigo.ataqueActual = this.ataques[nombreAtaque];
    }

    combate() {
        let resultado;

        if (this.jugador.ataqueActual.nombre === this.enemigo.ataqueActual.nombre) {
            resultado = "EMPATE";
        } else if (this.jugador.ataqueActual.venceA(this.enemigo.ataqueActual)) {
            resultado = "GANASTE";
            this.enemigo.recibirDano();
        } else {
            resultado = "PERDISTE";
            this.jugador.recibirDano();
        }

        this.interfaz.actualizarVidas(this.jugador.vidas, this.enemigo.vidas);
        this.interfaz.crearMensaje(this.jugador.ataqueActual.nombre, this.enemigo.ataqueActual.nombre, resultado);
        this.revisarVidas();
    }

    revisarVidas() {
        if (!this.enemigo.estaVivo()) {
            this.interfaz.crearMensajeFinal("FELICITACIONES!!! HAS GANADO 🤩🥳🎉");
        } else if (!this.jugador.estaVivo()) {
            this.interfaz.crearMensajeFinal("QUE PENA, HAS PERDIDO 😢😭😭😭");
        }
    }

    reiniciar() {
        if (this.jugador) this.jugador.resetear();
        if (this.enemigo) this.enemigo.resetear();
        this.interfaz.reiniciar();
    }

    aleatorio(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
    }
}

class Interfaz {
    constructor() {
        this.sectionSeleccionarAtaque = document.getElementById('seleccionar-ataque');
        this.botonPersonajeJugador = document.getElementById('boton-personaje');
        this.sectionReiniciar = document.getElementById('reiniciar');
        this.botonesAtaque = document.querySelectorAll('#seleccionar-ataque button');
        this.botonReiniciar = document.getElementById('boton-reiniciar');
        this.sectionSeleccionarPersonaje = document.getElementById('seleccionar-personaje');
        this.inputZuko = document.getElementById('zuko');
        this.inputKatara = document.getElementById('katara');
        this.inputAang = document.getElementById('aang');
        this.inputToph = document.getElementById('toph');
        this.inputSuki = document.getElementById('suki');
        this.inputIroh = document.getElementById('iroh');
        this.spanPersonajeJugador = document.getElementById('personaje-jugador');
        this.spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
        this.spanVidasJugador = document.getElementById('vidas-jugador');
        this.spanVidasEnemigo = document.getElementById('vidas-enemigo');
        this.sectionMensaje = document.getElementById('mensajes');
    }

    iniciar() {
        this.sectionSeleccionarAtaque.style.display = 'none';
        this.botonPersonajeJugador.addEventListener('click', () => this.seleccionarPersonajeJugador());
        this.sectionReiniciar.style.display = "none";

        document.getElementById("reglas-del-juego").style.display = "none";
        document.getElementById('boton-reglas').addEventListener('click', () => this.mostrarReglas());

        document.getElementById('boton-jugar').style.display = 'none';
        document.getElementById('seleccionar-personaje').style.display = 'block';

        this.botonesAtaque.forEach(boton => {
            boton.addEventListener('click', (event) => {
                const ataque = event.target.dataset.ataque;
                juego.realizarAtaque(ataque);
            });
        });

        this.botonReiniciar.addEventListener('click', () => this.reiniciar());
    }

    mostrarReglas() {
        document.getElementById("reglas-del-juego").style.display = "block";
        document.getElementById('boton-jugar').style.display = 'block';
        document.getElementById('boton-reglas').style.display = 'none';
        document.getElementById('seleccionar-personaje').style.display = 'none';
        document.getElementById('boton-jugar').addEventListener('click', () => this.seleccionarPersonajeJugador());
    }

    seleccionarPersonajeJugador() {
        this.sectionSeleccionarAtaque.style.display = 'block';
        document.getElementById('boton-reglas').style.display = 'none';
        this.sectionSeleccionarPersonaje.style.display = 'none';

        document.getElementById("reglas-del-juego").style.display = "none";
        document.getElementById('boton-reglas').style.display = 'none';

        let personajeSeleccionado = null;

        if (this.inputZuko.checked) {
            personajeSeleccionado = 'Zuko';
        } else if (this.inputKatara.checked) {
            personajeSeleccionado = 'Katara';
        } else if (this.inputAang.checked) {
            personajeSeleccionado = 'Aang';
        } else if (this.inputToph.checked) {
            personajeSeleccionado = 'Toph';
        } else if (this.inputSuki.checked) {
            personajeSeleccionado = 'Suki';
        } else if (this.inputIroh.checked) {
            personajeSeleccionado = 'Iroh';
        } else {
            this.mostrarError('Selecciona un personaje');
            return;
        }

        juego.seleccionarPersonajeJugador(personajeSeleccionado);
    }

    mostrarError(mensaje) {
        const mensajeError = document.createElement("p");
        mensajeError.innerHTML = mensaje;
        mensajeError.style.color = "red";
        this.sectionSeleccionarPersonaje.appendChild(mensajeError);

        setTimeout(() => {
            this.sectionSeleccionarPersonaje.removeChild(mensajeError);
        }, 2000);
        this.reiniciar();
    }

    mostrarSeleccionAtaque() {
        this.sectionSeleccionarAtaque.style.display = 'block';
    }

    mostrarPersonajes(nombreJugador, nombreEnemigo) {
        this.spanPersonajeJugador.innerHTML = nombreJugador;
        this.spanPersonajeEnemigo.innerHTML = nombreEnemigo;
    }

    actualizarVidas(vidasJugador, vidasEnemigo) {
        this.spanVidasJugador.innerHTML = vidasJugador;
        this.spanVidasEnemigo.innerHTML = vidasEnemigo;
    }

    crearMensaje(ataqueJugador, ataqueEnemigo, resultado) {
        const parrafo = document.createElement('p');
        parrafo.innerHTML = `Tu personaje atacó con ${ataqueJugador}, el personaje del enemigo atacó con ${ataqueEnemigo} ${resultado}`;
        this.sectionMensaje.appendChild(parrafo);
    }

    crearMensajeFinal(resultado) {
        this.sectionReiniciar.style.display = "block";

        const parrafo = document.createElement('p');
        parrafo.innerHTML = resultado;
        this.sectionMensaje.appendChild(parrafo);

        this.botonesAtaque.forEach(boton => {
            boton.disabled = true;
        });
    }

    reiniciar() {
        location.reload();
    }
}

let juego;

function iniciarJuego() {
    juego = new Juego();
    juego.interfaz.iniciar();
}
window.addEventListener('load', iniciarJuego);