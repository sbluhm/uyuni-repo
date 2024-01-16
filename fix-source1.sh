cd ~/git/uyuni
find . -type f -name "*.spec" -exec sed -i 's#Source1:        https://raw.githubusercontent.com/uyuni-project/uyuni/%{name}-%{version}-1/#Source1:        https://raw.githubusercontent.com/uyuni-project/uyuni/master/#' {} + | grep Source1
