PGDMP      .            
    {            loan_system_db    16.0    16.0 #               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            	           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            
           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16580    loan_system_db    DATABASE     �   CREATE DATABASE loan_system_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE loan_system_db;
                postgres    false            �            1259    16622    tb_balance_records    TABLE     �   CREATE TABLE public.tb_balance_records (
    id smallint NOT NULL,
    debtor_id smallint,
    running_balance numeric(8,2) NOT NULL
);
 &   DROP TABLE public.tb_balance_records;
       public         heap    postgres    false            �            1259    16621    tb_balance_records_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_balance_records_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.tb_balance_records_id_seq;
       public          postgres    false    222                       0    0    tb_balance_records_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.tb_balance_records_id_seq OWNED BY public.tb_balance_records.id;
          public          postgres    false    221            �            1259    16598    tb_debt_records    TABLE     %  CREATE TABLE public.tb_debt_records (
    id smallint NOT NULL,
    debtor_id smallint,
    debt_date date NOT NULL,
    debt_amount numeric(8,2) NOT NULL,
    interest_rate numeric(5,2) DEFAULT 0.10 NOT NULL,
    interest_amount numeric(8,2) NOT NULL,
    total_debt numeric(8,2) NOT NULL
);
 #   DROP TABLE public.tb_debt_records;
       public         heap    postgres    false            �            1259    16597    tb_debt_records_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_debt_records_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.tb_debt_records_id_seq;
       public          postgres    false    218                       0    0    tb_debt_records_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.tb_debt_records_id_seq OWNED BY public.tb_debt_records.id;
          public          postgres    false    217            �            1259    16591    tb_debtor_records    TABLE     �   CREATE TABLE public.tb_debtor_records (
    id smallint NOT NULL,
    name character varying(50) NOT NULL,
    age smallint,
    address character varying(100),
    phone_number character(11)
);
 %   DROP TABLE public.tb_debtor_records;
       public         heap    postgres    false            �            1259    16590    tb_debtor_records_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_debtor_records_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.tb_debtor_records_id_seq;
       public          postgres    false    216                       0    0    tb_debtor_records_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.tb_debtor_records_id_seq OWNED BY public.tb_debtor_records.id;
          public          postgres    false    215            �            1259    16610    tb_payment_records    TABLE     �   CREATE TABLE public.tb_payment_records (
    id smallint NOT NULL,
    debtor_id smallint,
    payment_date date NOT NULL,
    principal_paid numeric(8,2) NOT NULL,
    interest_paid numeric(8,2) NOT NULL,
    total_payment numeric(8,2) NOT NULL
);
 &   DROP TABLE public.tb_payment_records;
       public         heap    postgres    false            �            1259    16609    tb_payment_records_id_seq    SEQUENCE     �   CREATE SEQUENCE public.tb_payment_records_id_seq
    AS smallint
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.tb_payment_records_id_seq;
       public          postgres    false    220                       0    0    tb_payment_records_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.tb_payment_records_id_seq OWNED BY public.tb_payment_records.id;
          public          postgres    false    219            c           2604    16639    tb_balance_records id    DEFAULT     ~   ALTER TABLE ONLY public.tb_balance_records ALTER COLUMN id SET DEFAULT nextval('public.tb_balance_records_id_seq'::regclass);
 D   ALTER TABLE public.tb_balance_records ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            `           2604    16640    tb_debt_records id    DEFAULT     x   ALTER TABLE ONLY public.tb_debt_records ALTER COLUMN id SET DEFAULT nextval('public.tb_debt_records_id_seq'::regclass);
 A   ALTER TABLE public.tb_debt_records ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            _           2604    16641    tb_debtor_records id    DEFAULT     |   ALTER TABLE ONLY public.tb_debtor_records ALTER COLUMN id SET DEFAULT nextval('public.tb_debtor_records_id_seq'::regclass);
 C   ALTER TABLE public.tb_debtor_records ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            b           2604    16642    tb_payment_records id    DEFAULT     ~   ALTER TABLE ONLY public.tb_payment_records ALTER COLUMN id SET DEFAULT nextval('public.tb_payment_records_id_seq'::regclass);
 D   ALTER TABLE public.tb_payment_records ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220                      0    16622    tb_balance_records 
   TABLE DATA           L   COPY public.tb_balance_records (id, debtor_id, running_balance) FROM stdin;
    public          postgres    false    222   �*                 0    16598    tb_debt_records 
   TABLE DATA           |   COPY public.tb_debt_records (id, debtor_id, debt_date, debt_amount, interest_rate, interest_amount, total_debt) FROM stdin;
    public          postgres    false    218   �*       �          0    16591    tb_debtor_records 
   TABLE DATA           Q   COPY public.tb_debtor_records (id, name, age, address, phone_number) FROM stdin;
    public          postgres    false    216   +                 0    16610    tb_payment_records 
   TABLE DATA           w   COPY public.tb_payment_records (id, debtor_id, payment_date, principal_paid, interest_paid, total_payment) FROM stdin;
    public          postgres    false    220   %+                  0    0    tb_balance_records_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.tb_balance_records_id_seq', 1, false);
          public          postgres    false    221                       0    0    tb_debt_records_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.tb_debt_records_id_seq', 1, false);
          public          postgres    false    217                       0    0    tb_debtor_records_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.tb_debtor_records_id_seq', 1, false);
          public          postgres    false    215                       0    0    tb_payment_records_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.tb_payment_records_id_seq', 1, false);
          public          postgres    false    219            k           2606    16627 *   tb_balance_records tb_balance_records_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.tb_balance_records
    ADD CONSTRAINT tb_balance_records_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.tb_balance_records DROP CONSTRAINT tb_balance_records_pkey;
       public            postgres    false    222            g           2606    16603 $   tb_debt_records tb_debt_records_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.tb_debt_records
    ADD CONSTRAINT tb_debt_records_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.tb_debt_records DROP CONSTRAINT tb_debt_records_pkey;
       public            postgres    false    218            e           2606    16596 (   tb_debtor_records tb_debtor_records_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.tb_debtor_records
    ADD CONSTRAINT tb_debtor_records_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.tb_debtor_records DROP CONSTRAINT tb_debtor_records_pkey;
       public            postgres    false    216            i           2606    16615 *   tb_payment_records tb_payment_records_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.tb_payment_records
    ADD CONSTRAINT tb_payment_records_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.tb_payment_records DROP CONSTRAINT tb_payment_records_pkey;
       public            postgres    false    220            n           2606    16628 4   tb_balance_records tb_balance_records_debtor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_balance_records
    ADD CONSTRAINT tb_balance_records_debtor_id_fkey FOREIGN KEY (debtor_id) REFERENCES public.tb_debtor_records(id);
 ^   ALTER TABLE ONLY public.tb_balance_records DROP CONSTRAINT tb_balance_records_debtor_id_fkey;
       public          postgres    false    222    4709    216            l           2606    16604 .   tb_debt_records tb_debt_records_debtor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_debt_records
    ADD CONSTRAINT tb_debt_records_debtor_id_fkey FOREIGN KEY (debtor_id) REFERENCES public.tb_debtor_records(id);
 X   ALTER TABLE ONLY public.tb_debt_records DROP CONSTRAINT tb_debt_records_debtor_id_fkey;
       public          postgres    false    4709    218    216            m           2606    16616 4   tb_payment_records tb_payment_records_debtor_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_payment_records
    ADD CONSTRAINT tb_payment_records_debtor_id_fkey FOREIGN KEY (debtor_id) REFERENCES public.tb_debtor_records(id);
 ^   ALTER TABLE ONLY public.tb_payment_records DROP CONSTRAINT tb_payment_records_debtor_id_fkey;
       public          postgres    false    4709    216    220                  x������ � �            x������ � �      �      x������ � �            x������ � �     