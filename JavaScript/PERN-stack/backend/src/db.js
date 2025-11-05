import pg from "pg";

export const pool = new pg.Pool({
    port: 5173,
    host: "localhost",
    user: "postgresql",
    password: "admin",
    database: "PERN",
});

pool.on("connect", () => {
    console.log("Conectado a la base de datos");
});
