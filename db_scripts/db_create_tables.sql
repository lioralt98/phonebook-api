--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: phonebook; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA phonebook;


ALTER SCHEMA phonebook OWNER TO postgres;

--
-- Name: adminpack; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS adminpack WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION adminpack; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION adminpack IS 'administrative functions for PostgreSQL';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: contacts; Type: TABLE; Schema: phonebook; Owner: postgres
--

CREATE TABLE phonebook.contacts (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    middle_name character varying(50),
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE phonebook.contacts OWNER TO postgres;

--
-- Name: contacts_id_seq; Type: SEQUENCE; Schema: phonebook; Owner: postgres
--

CREATE SEQUENCE phonebook.contacts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE phonebook.contacts_id_seq OWNER TO postgres;

--
-- Name: contacts_id_seq; Type: SEQUENCE OWNED BY; Schema: phonebook; Owner: postgres
--

ALTER SEQUENCE phonebook.contacts_id_seq OWNED BY phonebook.contacts.id;


--
-- Name: contacts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.contacts (
    id integer NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    middle_name character varying(50),
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public.contacts OWNER TO postgres;

--
-- Name: contacts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.contacts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contacts_id_seq OWNER TO postgres;

--
-- Name: contacts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.contacts_id_seq OWNED BY public.contacts.id;


--
-- Name: phone_numbers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.phone_numbers (
    id integer NOT NULL,
    phone_number character varying(20) NOT NULL,
    phone_number_type character varying(20) DEFAULT 'None'::character varying NOT NULL,
    contact_id integer NOT NULL
);


ALTER TABLE public.phone_numbers OWNER TO postgres;

--
-- Name: phone_numbers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.phone_numbers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.phone_numbers_id_seq OWNER TO postgres;

--
-- Name: phone_numbers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.phone_numbers_id_seq OWNED BY public.phone_numbers.id;


--
-- Name: contacts id; Type: DEFAULT; Schema: phonebook; Owner: postgres
--

ALTER TABLE ONLY phonebook.contacts ALTER COLUMN id SET DEFAULT nextval('phonebook.contacts_id_seq'::regclass);


--
-- Name: contacts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts ALTER COLUMN id SET DEFAULT nextval('public.contacts_id_seq'::regclass);


--
-- Name: phone_numbers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_numbers ALTER COLUMN id SET DEFAULT nextval('public.phone_numbers_id_seq'::regclass);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: phonebook; Owner: postgres
--

ALTER TABLE ONLY phonebook.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (id);


--
-- Name: contacts contacts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.contacts
    ADD CONSTRAINT contacts_pkey PRIMARY KEY (id);


--
-- Name: phone_numbers phone_numbers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_numbers
    ADD CONSTRAINT phone_numbers_pkey PRIMARY KEY (id);


--
-- Name: phone_numbers phone_numbers_contact_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.phone_numbers
    ADD CONSTRAINT phone_numbers_contact_id_fkey FOREIGN KEY (contact_id) REFERENCES public.contacts(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

