CREATE PROCEDURE concatenar_colores()
BEGIN
    DECLARE fin INT DEFAULT 0;
    DECLARE color VARCHAR(10);
    DECLARE cursor_colores CURSOR FOR SELECT nombre FROM colores;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

    OPEN cursor_colores;

    read_loop: LOOP
        FETCH cursor_colores INTO color;
        IF fin = 1 THEN
            LEAVE read_loop;
        END IF;
        SELECT CONCAT('Color: ', color);
    END LOOP;

    CLOSE cursor_colores;
END;

