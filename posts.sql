--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

-- Started on 2023-03-30 00:15:38

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16450)
-- Name: posts; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    content character varying NOT NULL,
    published boolean DEFAULT true NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.posts OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16449)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_id_seq OWNER TO postgres;

--
-- TOC entry 3330 (class 0 OID 0)
-- Dependencies: 216
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- TOC entry 3176 (class 2604 OID 16453)
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- TOC entry 3324 (class 0 OID 16450)
-- Dependencies: 217
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.posts (id, title, content, published, created_at) FROM stdin;
3	Hello!	 then people wont probably read more than word or two. Dont be a writer who makes even the most amazing experiences like a thesis but like those who can make even snoring sound like skydiving!	t	2023-03-12 18:32:32.93477+05:30
4	approach	Spain’s jobless rate for people ages 16 to 24 is approaching 50 percent.	t	2023-03-12 18:42:21.040237+05:30
5	concern	The scandal broke out in October after former chief executive Michael Woodford claimed he was fired for raising concerns about the company's accounting practices.	t	2023-03-12 18:46:10.496738+05:30
2	evident	That confidence was certainly evident in the way Smith handled the winning play with 14 seconds left on the clock.	t	2023-03-12 18:13:24.187274+05:30
6	concern	The scandal broke out in October after former chief executive Michael Woodford claimed he was fired for raising concerns about the company's accounting practices.	t	2023-03-13 23:33:39.05569+05:30
\.


--
-- TOC entry 3331 (class 0 OID 0)
-- Dependencies: 216
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.posts_id_seq', 6, true);


--
-- TOC entry 3180 (class 2606 OID 16459)
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


-- Completed on 2023-03-30 00:15:40

--
-- PostgreSQL database dump complete
--

