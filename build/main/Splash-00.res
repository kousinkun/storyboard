tcl86t.dll      tk86t.dll       _tk_data             �  %�  �  �   Hapi-ms-win-core-fibers-l1-1-0.dll _tk_data\ttk\ttk.tcl api-ms-win-crt-math-l1-1-0.dll api-ms-win-core-localization-l1-2-0.dll _tk_data\ttk\cursors.tcl api-ms-win-core-sysinfo-l1-1-0.dll api-ms-win-core-timezone-l1-1-0.dll ucrtbase.dll api-ms-win-core-profile-l1-1-0.dll api-ms-win-core-memory-l1-1-0.dll api-ms-win-crt-stdio-l1-1-0.dll api-ms-win-core-synch-l1-1-0.dll api-ms-win-crt-utility-l1-1-0.dll _tk_data\tk.tcl api-ms-win-crt-string-l1-1-0.dll api-ms-win-core-heap-l1-1-0.dll api-ms-win-core-processenvironment-l1-1-0.dll api-ms-win-core-datetime-l1-1-0.dll api-ms-win-core-string-l1-1-0.dll VCRUNTIME140.dll _tk_data\text.tcl _tk_data\ttk\fonts.tcl tk86t.dll api-ms-win-crt-convert-l1-1-0.dll api-ms-win-core-console-l1-1-0.dll api-ms-win-crt-runtime-l1-1-0.dll api-ms-win-crt-time-l1-1-0.dll api-ms-win-core-file-l1-1-0.dll api-ms-win-crt-heap-l1-1-0.dll api-ms-win-crt-environment-l1-1-0.dll api-ms-win-core-interlocked-l1-1-0.dll api-ms-win-core-processthreads-l1-1-1.dll api-ms-win-core-debug-l1-1-0.dll tcl86t.dll _tk_data\license.terms api-ms-win-core-rtlsupport-l1-1-0.dll api-ms-win-core-file-l2-1-0.dll _tk_data\ttk\utils.tcl api-ms-win-core-handle-l1-1-0.dll api-ms-win-core-libraryloader-l1-1-0.dll api-ms-win-core-file-l1-2-0.dll api-ms-win-core-namedpipe-l1-1-0.dll api-ms-win-core-synch-l1-2-0.dll api-ms-win-core-errorhandling-l1-1-0.dll api-ms-win-core-util-l1-1-0.dll api-ms-win-core-processthreads-l1-1-0.dll proc _ipc_server {channel clientaddr clientport} {
set client_name [format <%s:%d> $clientaddr $clientport]
chan configure $channel \
-buffering none \
-encoding utf-8 \
-eofchar \x04 \
-translation cr
chan event $channel readable [list _ipc_caller $channel $client_name]
}
proc _ipc_caller {channel client_name} {
chan gets $channel cmd
if {[chan eof $channel]} {
chan close $channel
exit
} elseif {![chan blocked $channel]} {
if {[string match "update_text*" $cmd]} {
global status_text
set first [expr {[string first "(" $cmd] + 1}]
set last [expr {[string last ")" $cmd] - 1}]
set status_text [string range $cmd $first $last]
}
}
}
set server_socket [socket -server _ipc_server -myaddr localhost 0]
set server_port [fconfigure $server_socket -sockname]
set env(_PYI_SPLASH_IPC) [lindex $server_port 2]
image create photo splash_image
splash_image put $_image_data
unset _image_data
proc canvas_text_update {canvas tag _var - -} {
upvar $_var var
$canvas itemconfigure $tag -text $var
}
package require Tk
set image_width [image width splash_image]
set image_height [image height splash_image]
set display_width [winfo screenwidth .]
set display_height [winfo screenheight .]
set x_position [expr {int(0.5*($display_width - $image_width))}]
set y_position [expr {int(0.5*($display_height - $image_height))}]
frame .root
canvas .root.canvas \
-width $image_width \
-height $image_height \
-borderwidth 0 \
-highlightthickness 0
.root.canvas create image \
[expr {$image_width / 2}] \
[expr {$image_height / 2}] \
-image splash_image
wm attributes . -transparentcolor magenta
.root.canvas configure -background magenta
pack .root
grid .root.canvas -column 0 -row 0 -columnspan 1 -rowspan 2
wm overrideredirect . 1
wm geometry . +${x_position}+${y_position}
wm attributes . -topmost 1
raise .�PNG

   IHDR  9   �   G�   sRGB ���   gAMA  ���a   	pHYs    �&�?  %{IDATx^�x���A����"("*"E�4A����/ "
�VV,(ґJBhI�@�#=�J�u�y��&{7��Mrq��=�<�ݳ}ϻ3��97)��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��i�%r��' ;������+��e/��QBQ%��K�jM��՜C2�J櫵�f�L��Q1�q�J���(JpI���4*0�?�>_���*�f�R�?���0��N�n�PE	.���c3�gg�3�J楹�)�@6k��!�ȔF	EQ���5"���Є�t��cK*r��\j�F䆌��#����#Ɩ>T�E��d���X�Bw�[�P�S�R��b���A�����Ɩ>T�E��d^���'Dѵ�C%LM^B���2���"�(ʥ&�"7(�Z�[BFOH!r��N��|P�S�R�y�8�z�YO%'L�.i9޵#Bi~�Ac����a@ƉE�a�[Q��A���o����Ir�uX�M���������丽Yd�^Z|�0�;z��N���b��̶�8I�l���WP�Y�j�L���YiJ���|�"is��p�2w4EQ����ܯc�[�o����0�N��������r�9. ��x��0�iT8U`!z����P������ڈ�}�(f>�g|�5�x�����_��F��Sg��(���ȼ�I�m�J���+��X�D̠�}�]�"O�<C���k!�Y�~a���+-�?IM�c��Q�~���f(��Y;z�2�SQ��CPD^�/o3�'0���*r�/�Me&N�u
�������7��̌}	Td�d߹*nv�cͳ�?*��=����~��/3	��/r��	�>P�����:��\��m�a��2�q�|\7 LB&�<o���:�����{��*��]�ȡ����A��Y�X�A�*r��������3�����(ze�R�?c�?>җ��&�,>EB�8�q���Y���<g�/7�Cͩ��X�D���a���(ه���o�bS
�ں@�"����>�Z�4��7m5J>w��m�*�"��F>{��"��KV��;m������ּ�'N�U�o�Q�ҳ�(J�"�"�4��v�a�z��X�I�I"Qi�y��=�0Ks�bB΋쥕����J��h��E�����)�0Y�b���Y;,֦�X1��7��H�CQ��EPE�L!4�[����;2�6;.a_Z"�x�<��tW��Ȋ�s�^�����ʑ3Sz�0W�9����V8��mBh��x�����������MF�(J� �"!���)Ā�?i��߂�Ebx�xX�2��W���mkh�sF^V~�����?s�
������2���Fi�x�=n���K����#��=	�ȁ7��� r���^@�"������1�Cخ�V%�Y�x�nD�h�0����]�s�{�Z�aci��ı��4^����FIEQ�A��[w��:�s�� ��OW�s.;$v�Q2�T�����ʿ��>�aQ¾��x�@��r�y㺬���2A��)��=	�ȭ;r�r�9�_�����G�33�#��՛1ODƯ���0r���F�d���B<M��÷�4J��t�x���a|,���?z����
��D������j�{D[��(ٗ��܉�hXD
O	ӡ���f��.R��(g/��w;z>e*HØ���Y�O���E7��4�j3i��S�v���bX��U%�t�� wIIKDL����ģtSHxJ!4�մM�	���7c/�YCDp���Lb�%�rޜ�c5���Z2;�����|O�:)����iԓ'O҅L��N��~Ndj?�ᔜ�	:��!gΜ��'Nйsg�%�s��E:����,�GI֭�)�i��5��?�DO�U˗���:̂.r����G�YD.tW�t+N��k��tȌ!N���<�b��Yigs
���e��\� �@X�/Y�:���3OӦ�ߦ={�,��M�K[�l��Z���իд�Y��;F��hNOT�DS#�Ȳ�K�P�>?Ҝ���'�ϙM��3��o4�_i��"Nijٴ	=Q�"���X�χ�v�G�?L?|���$pf͈�g�x\�˧=ޗ���ի菾��u�mP��h����w��`x��A(�/��;j����cy7�~�vl�.�9���to19>�Ç|c�c7o�~?��X��pV.[J���ɑ��v�@�ǌ����O=I'��q�wQ�_�wlX>���0�>Px���{�T��p���3J��ܤ�=�yJ0�\�O�>Y�ν��E�)-d�.���8�M������'�9^��p0�x}n�7ܖ7�Q�.ZH��(@��V._&�K�3�u4wV�x��.��S�g�#��T�li�w�U4��a���/zQ�+rP����v6�׾R���������_��:���/���P�Dq�9wN������6Z4nH�sE��r��7�
ݜW�K��O�;��s�����|7R��n�mͿq���)Iw�x=��w�2�����;o���}V���Y�����}j��ݷ�DQ�'�~V�X!��T��p��d���[)a,N���t*�fx��~ً���s�%�U���4~�Y�����>2����x�������=�T��RT��SY'�yFO���3J��\,߸����݌E��!r�Aj�0w��f�8Ze��C��SWa�}�;LP)�Z�F�i�����[rFX�b9����,z���0{��>BE��%�S�V�J�/cFA���%���ѝ�徂�~����ʶ��T��*�R>|��ԪY�_�	9��
�&_`'�=��&�J+>���z}�!?~�+�q���n֔�%�۩��$p&������*��Z�~�uDa�$�ޞ�J��J�[D�Ʋ�?�)g�[o�gQ�x1*�@�����| p] ��a�V���&�o5����ͺ���%������گ����}O�[��'���m���N۸�y����9��n�2��֛2�n�u�<��־\�y�8_�u=�Yçk�> r���w�Z�n؇y_����}F��C�\�I�=�v9C��^��������8�?4me��Ȇ��C��C��9?����cd3��#G�<n�Hz�;�D���Eݰ�/Z�r=�/�ӏV��x�~⑊Դ^]+jї=?��E�ņ�Q�zud���+� W`�~*�2T��/4�];��p 3�F��B�p3�ˉp0�=��_n-/�}��|��3:x�?t�"R���B���O��B�g)>n�Q2m��x����WV����$r��!>��eO���6E����F*$D�ǽ�'�q�wi�֭l�I�-6�C�mt�
�p}���w_~A?��J�G6xH���Ǹ����B}��T0��n�Տ}{��7�y�z'������#��V�C�Zoh��R�oz}.�\o~~����Qv��6���x �~���3�����7ul�*݋���G+������2��=mD$��!|����h7l��<R��\?Dn��f�,9��|��Н�ţZ�LZs�(]�6��Cպ�s�F- xV�	#:$���R`l-ʧ؇��Z��!dąT���w��`~�PQ�֯��j��h+1+���z^�!^���~&$��������Tf,�骜��_���vH�?�}�V:����8A֛@L^m�py?5�T���͜6U�2H֙ǂ�1B�[���}[�!-�[�b߸�S�L����0���5�1�@�� O�^����e`����[��M��hᘸ�����+m��������(�p|fN�f,�;����XE.;2k�ty����l�ص3-=�)��'k��˶��y����6Vcq�15F�J �8�k���a��U���D�b �&�Ƒ.��M��"�PCVS��u���ᅆ��n�7���5g�_�n�;џ��~�;�I�n�A�wd���Rc?�o=,���-
=J��Ft�	m��<%����a`�]�GĢzQw��IS&�KHC'G��?����x��d��M�fr�now2����Hl�v|���������b��B�.;ȾL�+�egϜ!�2���GBi��h�z�}[Y?{ft���q��t�6��\?�/S�Ef���
�����EO�L9|@���^z|�L�˖mr`^�!�T�i���,�5��c,>cw&�=&�c��l��k%�$d�n�u'����4}�o����H����<����9PJ��pa<���c%\mٴ�4l�KC[Z�ʕ䥙��/�9�`�ޑ����;���?x?�h�@D�~h�G8=�f��C(lL���C��իR����:����ժV����S�_^WM�!b��O�����'OolE�r�2�ZU+K�i(�+���hOJ��~��X.���9T��}~q�Ǻq�:y9�B-x�(���qjU{�=�}�/72#rK-�K�:�۸�ܬ�h�]������A���ͥ���S:8�!�D�ڑ��f�R���z�R6{k��S6�vX�>�HN�Нq2[�|�+��Ma9�$�������F؜�x�}�#3,r&h�@����=�Oi'AnڰjT,//Mȟ�ċB[���ؑkg.Ki��h,�Q��x/;�1DC0��Ng���Y�\=�h'��E޽s�k���ӭ��O���K�.��o�I*^^xt��N`��F��1��Iv�=��Y�ѐ�C�<����ˡ�i���x�h��=xW!i�B[�)rX?�iCT,�pg���G!�Hc8���r/�DH�o8?W�0�fY�?O.�𽮲�`�"�vU�y]R�������:_/�̭�XT����Lc�*��R4	��1��
"X<<��Z~����q�cL��pv��]�c�Z� �j��V���>�,�g�����}���d��3
��@��u:���>{G�_nM�Z���͚P�{��O��˭�-[P�7^�|)!|_y�j����K���.oӎm�$��$rV��o�� 
� $��t�B�9F(�u�Oi��Yԓ����ѣ��J��{i?��Z�x���;�ϝ��(��3=��0E�1:*�ױ���g<H�˕�s��F{Z0w���[;����a��5+E��C1��w~[R� r%!r���g���*pmny���a��v��$d��G7����O{t�5+�S��B�m /�����"�aF��.�11�^ﴝiS���/j�6!%F@���' ]=E9L�>%n��9��Vf��;��vV0�1��˚������Q��2�/!*a9���F���Y^R^O��ً�۵KD����m̜#T��]-_����M����͛I�VZ"w���C\�:���;L�U˗Q]c�q!�ڳ
 �h7C�^z@xY�L)���7�	꧆)r�7�x>x��#�%.�?O<5��*ѻ��O��@tV����}B�OދO?I�wӪ˥���q?������ۺe��-�7W�zl��=cF�:l�N$��<ΑB~K\�A����+Y!r�x�\��\G��󹧌�C�D.��m��X���_跳��a	C�aal�6k��h�L�d����������z}å���V�"���0-*�����m?������C��۷���ܕ,r\/N��]��9r$QD���q��m0
�p���R`t. �cO|<�z����aXپ�{�"#"�����Y��?�Hp�H?Ań5a/2>�?y;�yr�"�$���ǁ+T�7ߐ{�U�l�(�X� ��z�q(\P<g�	2�/�ȡ���F�z\D��ڵ$�� ����o�fN�Ɂ��T�T	��GJ����Q�s��	���A��5:�/�B�fL�*�"W�RJ����B��H�mmg�����m��u}�v�t( ,�3?G��І�9��s�u�IŁ��U�L>Y��t: ���-L�{O�/�7S9Eh�j�^���g��K�@DigP��E,���p~/4�/�>d�d��+����H~��o�IFD(��+� �-�}��iC*!�����Sn��DG<9T$$��!tr�i]
�3�sB��Q�����\�@A+F��+�,!��3r�c��S�t؏ҁ�i��G�L�B�Ф`�����,�n\v�C���׶��G���t@ZH�(Lw��b�/�l�r��S��SSZx$}�n�_���=	�ܩ|�������0r�P�XhWA/#ڭг�v:��D8۰�S�����+_���r��`D	�V�b��!-�d;xq�!�
��	^E��d�a�T��d���/|���� ����v�9�g#odD� ��p%j\�i�^��y�-�S�p>+�-��ɓ�W�zt�,"��m�Jk�˗-YL_��Dگ��%��z�3�㗟�>�'B�ô�� �.~WA�?�ʖ��7�	��a�-�����s�s�E.�=�{�ܧh�����F�%�f+c�l3�v�<-�Ynw�'O{��;N�r,�e�cg���Ƞ�5�V&�2=8��TH<\�������Ǯ���ȁ{-9m��@ϥ��W��"��8/^��9F����V��?��͞�'���"��k�� k��Ff ��@o�̕K?$��6��94����h.�x�*(��~$ڜ�5���%��+xx��	7�)r �3x tx|Qz�eZD�\3���f5�9x�H���G��Z�CO~f��"���r�R�`,r��P"E���7o�����9���F����2����)2Ւ��	��T���#\z0QD��q�S���s���v��?g���ڦ��*�!�G�/Ѥ��C[R9���� �\�`��4%ȃ�KZ�li:d�xa"	�@EN�h,��y��D�0���d�M��űH�}
�O�ok&�bhD������q�܊U�H�p�}8��{��o��)���y}H���/L� �7�6?L��L%�k�1ǳǵ�y�z��=&�-k��Y�/�_荿K�����KM�3���:�/F�`֙�p�Eә�62"��P�adX�l�n�p��#�e��4Wȹ	i�����^���ȿ��9�8�C��l�33?T��*r�֬���*��		�k��C�6B��9�B�zͼ6+�Y"��O�'��z�ww�=��h�kմ��`l��!E"�5_�
<�N��Rޜ9���
�cT2���	T�0�@�A��� �[6'�)]�c���k��C�0���&��A�06B�YV����|���xb�3�M�lC�DZ@+grX�-<���N:_��C8�q��n�����:R�N+�X�u�ԤQ�秃(b�R|�|���������M�a�(�]�:���d7'��4�c�C�	~5����"5�Ocw�ɿN��x�Srf��ܦ�d"Û��c�t�*��x+��˿y�F�X�A�����A��'9K������1(��\9�>?J٘���L�W�ȼ`vڶj!)��M�	a�BcJ����m���\Z)$�vxUh�C��=@�F���,L���7��-5���}&ﰗ��T�\v��hմ��5=��Q��0�A"��k֔���1�Jq9>Dn��~�af�����)�"�b#�q�{�b�I�:��7��\��� x���sG[e�NoH>\0��n8w���9x���y�7�;j/�6e�&�>��1��2_��cN�bw���M����||�q]xH��(�]�q�Q�@L�m]�^��KW�q���'
1���V�﫦װ]�%+��*��]� dȁ3ƣ]��1#G�2T\���@Z@��J:^ �\0t����6=s��;{�DH@�BO�L���ʎ4���7��FZ^��H��X�X�=�N"7෾I���d�%�#���c���1��ʊ�c���X�2�s�68��Fo�9�����)�<V]�[�6@3 ���a�CT��_l&�ld�Do8��XV���m�����~�9�8�X���p��8TF���#��0�kB�ψ��e{���ZI�u����FO4Ft�'ؿ��p\��q���qnx��F�N�g����>�^<P�yw�ႝ��O���ÌrYEӒߊy��B�R3���qY�n	�m�����\J0i��o3&C\#_u�z0A�B�dX'�ĸW�x��ɀt~�E
��4 \�uzSڪfϜ)� �4A&�M-�/"F/@T0�:%�hAE�� ��
/��̗Mā�N��U����ꊧ ���[��0x]8*���]�K5�L�6`^v�����^C ��f��H��Q8g��� �H���H���猶4rcFT:&z�D(3�N2���̶�é  C� z�q2��b�H���n�����p��8t3��ŕ��xf����v��������+��zmb�f�=��ǹ!���9���>%��Ѯ�R�47&�8�<�x�:��>�6R7.��ᗰJL����A�n��hL��a\-�.����xK��iP�v��)��b=���_s��2vf��UR�Ѩ���a�<� �JՇK�۴G �Ob3~������`��%�"��:̶���J��_�oW�X^�M0K
��D�v�Q����"��jז��Q���V�[�1	��^�����2���u��3�Ϸ����b(Z��e��s�^f�E�D�Mʶ����bDN�Dm[�dO�5�f��Ҩ���:R3x��h���p)I�i�L�?zխ�g�c�m�o]���A��8�/> �7��O>J
ӳ
LC�w�~}i:S�S�魶�n���&�ҁ:�چ~����;���x�	Y��J������*rH�8x�\���_��1��T7�z'��M@[	&��8E{Z�X �@(������EX��T��&XĀy�K+�����^̔4h#��0�{0�*��:Љ*Q޼�H��>�|��2?S�����Gu�j���IONQ%�Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<����(�FENQO�"�(��Q�S�Ө�)��iT�E�4*r��x9EQ<��?����M�    IEND�B`�