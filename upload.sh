sudo pip3 uninstall -y MyCryptoKeys
sudo python3 setup.py build sdist bdist_wheel
sudo python3 setup.py install
python3 -m twine upload --skip-existing --verbose dist/*