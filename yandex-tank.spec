%define _builddir	.
%define _sourcedir	.
%define _specdir	.
%define _rpmdir		.

Name:		yandex-tank
Version:	1.4.6
Release:	6

Summary:	Yandex.Tank (Load Testing Tool)
License:	MIT
Group:		System Environment/Libraries
Distribution:	Red Hat Enterprise Linux

BuildArch:	noarch

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	python-psutil
Requires:	python-progressbar
Requires:	python-ipaddr

%description
Yandex.Tank (Load Testing Tool)


%prep


%build


%install
%{__rm} -rf %{buildroot}

install -d -m 755 %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/agent
install -d -m 755 %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg
install -d -m 755 %{buildroot}/usr/lib/yandex-tank/Tank/stepper
#Tank/MonCollector/agent
#Tank/Plugins
install -d -m 755 %{buildroot}/etc/yandex-tank

install -m755 Tank/ConsoleWorker.py %{buildroot}/usr/lib/yandex-tank/Tank/ConsoleWorker.py
install -m755 Tank/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/__init__.py
install -m755 Tank/MonCollector/collector.py %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/collector.py
install -m755 Tank/MonCollector/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/__init__.py
install -m755 Tank/MonCollector/agent/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/agent/__init__.py
install -m755 Tank/MonCollector/agent/agent.cfg %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/agent/agent.cfg
install -m755 Tank/MonCollector/agent/agent.py %{buildroot}/usr/lib/yandex-tank/Tank/MonCollector/agent/agent.py
install -m755 Tank/Plugins/ConsoleScreen.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/ConsoleScreen.py
install -m755 Tank/Plugins/Autostop.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Autostop.py
install -m755 Tank/Plugins/ShellExec.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/ShellExec.py
install -m755 Tank/Plugins/Monitoring.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Monitoring.py
install -m755 Tank/Plugins/jmeter_writer.xml %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/jmeter_writer.xml
install -m755 Tank/Plugins/TotalAutostop.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/TotalAutostop.py
install -m755 Tank/Plugins/monitoring_default_config.xml %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/monitoring_default_config.xml
install -m755 Tank/Plugins/Codes.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Codes.py 
install -m755 Tank/Plugins/WebOnline.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/WebOnline.py
install -m755 Tank/Plugins/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/__init__.py
install -m755 Tank/Plugins/tips.txt %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/tips.txt
install -m755 Tank/Plugins/Loadosophia.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Loadosophia.py
install -m755 Tank/Plugins/GraphiteUploader.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/GraphiteUploader.py
install -m755 Tank/Plugins/Aggregator.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Aggregator.py
install -m755 Tank/Plugins/TipsAndTricks.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/TipsAndTricks.py
install -m755 Tank/Plugins/phantom_benchmark_additional.tpl %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/phantom_benchmark_additional.tpl 
install -m755 Tank/Plugins/ConsoleOnline.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/ConsoleOnline.py
install -m755 Tank/Plugins/ResourceCheck.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/ResourceCheck.py
install -m755 Tank/Plugins/phantom_benchmark_main.tpl %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/phantom_benchmark_main.tpl
install -m755 Tank/Plugins/PhantomUtils.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/PhantomUtils.py
install -m755 Tank/Plugins/ApacheBenchmark.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/ApacheBenchmark.py
install -m755 Tank/Plugins/Phantom.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Phantom.py
install -m755 Tank/Plugins/online.html %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/online.html
install -m755 Tank/Plugins/JMeter.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/JMeter.py
install -m755 Tank/Plugins/phantom.conf.tpl %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/phantom.conf.tpl
install -m755 Tank/Plugins/bfg/guns.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/guns.py
install -m755 Tank/Plugins/bfg/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/__init__.py
install -m755 Tank/Plugins/bfg/plugin.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/plugin.py
install -m755 Tank/Plugins/BFG.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/BFG.py
install -m755 Tank/Plugins/bfg/reader.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/reader.py
install -m755 Tank/Plugins/bfg/widgets.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/widgets.py
install -m755 Tank/Plugins/bfg/worker.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/bfg/worker.py
install -m755 Tank/Plugins/graphite.tpl %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/graphite.tpl
install -m755 Tank/Plugins/jmeter_argentum.xml %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/jmeter_argentum.xml
install -m755 Tank/Plugins/RCAssert.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/RCAssert.py
install -m755 Tank/Plugins/Report.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Report.py
install -m755 Tank/Plugins/UniversalPhoutShooter.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/UniversalPhoutShooter.py

#install -m755 Tank/stepper/Stepper.py %{buildroot}/usr/lib/yandex-tank/Tank/Plugins/Stepper.py
install -m755 Tank/stepper/config.py  %{buildroot}/usr/lib/yandex-tank/Tank/stepper/config.py
install -m755 Tank/stepper/util.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/util.py
install -m755 Tank/stepper/mark.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/mark.py
install -m755 Tank/stepper/missile.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/missile.py
install -m755 Tank/stepper/load_plan.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/load_plan.py
install -m755 Tank/stepper/instance_plan.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/instance_plan.py
install -m755 Tank/stepper/format.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/format.py
install -m755 Tank/stepper/info.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/info.py
install -m755 Tank/stepper/main.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/main.py
install -m755 Tank/stepper/__init__.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/__init__.py
install -m755 Tank/stepper/module_exceptions.py %{buildroot}/usr/lib/yandex-tank/Tank/stepper/module_exceptions.py
install -m755 tankcore.py %{buildroot}/usr/lib/yandex-tank/tankcore.py
install -m755 tank.py %{buildroot}/usr/lib/yandex-tank/tank.py
install -m755 *.sh %{buildroot}/usr/lib/yandex-tank/
install -m644 00-base.ini %{buildroot}/etc/yandex-tank/00-base.ini
#Tank usr/lib/yandex-tank

%clean
rm -rf $RPM_BUILD_ROOT

%post
chmod 777 /var/lock
if [ $1 -eq 1 -o $1 -eq 2 ] ; then
	if [ ! -e /usr/bin/lunapark ] ; then
		ln -sf /usr/lib/yandex-tank/tank.py /usr/bin/lunapark
	fi
	if [ ! -e /usr/bin/yandex-tank ] ; then
        	ln -sf /usr/lib/yandex-tank/tank.py /usr/bin/yandex-tank
	fi
	if [ ! -e /usr/bin/yandex-tank-ab ] ; then
        	ln -sf /usr/lib/yandex-tank/ab.sh /usr/bin/yandex-tank-ab
	fi
	if [ ! -e /usr/bin/yandex-tank-jmeter ] ; then
        	ln -sf /usr/lib/yandex-tank/jmeter.sh /usr/bin/yandex-tank-jmeter
	fi
fi

%preun
if [ $1 -eq 0 ] ; then
	rm -f /usr/bin/lunapark /usr/bin/yandex-tank /usr/bin/yandex-tank-ab /usr/bin/yandex-tank-jmeter
fi

%files
%defattr(-,root,root)
%dir %attr(0755,root,root) /usr/lib/yandex-tank
%dir %attr(0755,root,root) /etc/yandex-tank
%attr(0755,root,root) /usr/lib/yandex-tank/*

%attr(0644,root,root) /etc/yandex-tank/00-base.ini
