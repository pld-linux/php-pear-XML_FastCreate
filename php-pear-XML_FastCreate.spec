%define		status		stable
%define		pearname	XML_FastCreate
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - fast creation of valid XML with DTD control and translation options
Summary(pl.UTF-8):	%{pearname} - szybkie tworzenie poprawnego XML-u ze sprawdzaniem DTD i opcjami dla tłumaczeń
Name:		php-pear-%{pearname}
Version:	1.0.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	1ecd15f5619aa9fa3324e48ec0458583
URL:		http://pear.php.net/package/XML_FastCreate/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(core) >= 4.3.2
Requires:	php-pear
Suggests:	php-pear-XML_Beautifier >= 1.1
Suggests:	php-pear-XML_DTD >= 0.4.1
Suggests:	php-pear-XML_HTMLSax >= 2.1.2
Suggests:	php-pear-XML_Tree >= 2.0-0.b2
Obsoletes:	php-pear-XML_FastCreate-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(XML/Tree.*) pear(XML/DTD.*) pear(XML/Beautifier.*) pear(XML/HTMLSax.*)

%description
Key features of this package include:
- Easy way to make valid XML :
	$x->div(
	$x->h1("Example"),
	$x->p("Hello"),
	$x->p(array('class'=>'example'), "World !")
	)

- Option to report DTD errors in your XML :
Use internal tool or external program [ Require XML_DTD package ]

- Use output driver of your choice :
Text : return string
XML_Tree : return XML_Tree object [ Require XML_Tree package ]

- Translate option to quickly transform tags by anothers :
ex: Convert your XML to XHTML :
<news><title>Example</title></news>
to :
<div class="news"><h1>Example</h1></div>

- Include a PHP program to quickly transform HTML to FastCreate syntax.
[ Require XML_HTMLSax package ]

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Kluczowe możliwości tego pakietu obejmują:
- prosty sposób tworzenia poprawnego XML-a:
	$x->div(
	$x->h1("Przykład"),
	$x->p("Witaj"),
	$x->p(array('class'=>'example'), "Świecie!")
	)

- opcję zgłaszania błędów DTD w XML-u:
użycie wewnętrznego narzędzia lub zewnętrznego programu (wymaga
pakietu XML_DTD)

- użycie wybranego sterownika wyjściowego:
Text : return string
XML_Tree : return XML_Tree object
(wymaga pakietu XML_Tree)

- opcję tłumaczenia szybko przekształcającą znaczniki przez inne, np.
w celu przetłumaczenia XML-a na XHTML:
<news><title>Przykład</title></news>
na:
<div class="news"><h1>Przykład</h1></div>

- dołączanie programu PHP do szybkiego przekształcania HTML-a do
składni FastCreate (wymaga pakietu XML_HTMLSax).

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/XML_FastCreate/README .

install -d ./%{_bindir}
mv ./{%{php_pear_dir}/script/HTML2XFC.php,%{_bindir}/HTML2XFC}

install -d ./%{php_pear_dir}/tests/%{pearname}
mv ./%{php_pear_dir}/{XML/tests/*,tests/%{pearname}}

install -d ./%{php_pear_dir}/data/%{pearname}
mv ./%{php_pear_dir}/{XML/dtd/*,data/%{pearname}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
install ./%{_bindir}/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc README
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/HTML2XFC
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/FastCreate
%{php_pear_dir}/data/XML_FastCreate
