#############################################################################
# Generated by PAGE version 4.14
# in conjunction with Tcl version 8.6
set vTcl(timestamp) ""


if {!$vTcl(borrow)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #d9d9d9
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(active_menu_fg) #000000
}

#############################################################################
#################################
#LIBRARY PROCEDURES
#


if {[info exists vTcl(sourcing)]} {

proc vTcl:project:info {} {
    set base .top37
    global vTcl
    set base $vTcl(btop)
    if {$base == ""} {
        set base .top37
    }
    namespace eval ::widgets::$base {
        set dflt,origin 0
        set runvisible 1
    }
    set site_4_0 .top37.tNo39.t0 
    set site_4_0 $site_4_0
    set site_5_0 $site_4_0.scr43
    set site_4_1 .top37.tNo39.t1 
    set site_4_0 $site_4_1
    namespace eval ::widgets_bindings {
        set tagslist _TopLevel
    }
    namespace eval ::vTcl::modules::main {
        set procs {
        }
        set compounds {
        }
        set projectType single
    }
}
}

#################################
# GENERATED GUI PROCEDURES
#

proc vTclWindow.top37 {base} {
    if {$base == ""} {
        set base .top37
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 900x927+575+46
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 5764 1057
    wm minsize $top 140 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "BCS Message Converter"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    ttk::style configure TNotebook -background #d9d9d9
    ttk::style configure TNotebook.Tab -background #d9d9d9
    ttk::style configure TNotebook.Tab -foreground #000000
    ttk::style configure TNotebook.Tab -font TkDefaultFont
    ttk::style map TNotebook.Tab -background [list disabled #d9d9d9 selected #d9d9d9]
    ttk::notebook $top.tNo39 \
        -width 854 -height 821 -takefocus {} 
    vTcl:DefineAlias "$top.tNo39" "TNotebook1" vTcl:WidgetProc "Toplevel1" 1
    frame $top.tNo39.t0 \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    vTcl:DefineAlias "$top.tNo39.t0" "TNotebook1_t0" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo39 add $top.tNo39.t0 \
        -padding 0 -sticky nsew -state normal -text {Convert   } -image {} \
        -compound left -underline -1 
    set site_4_0  $top.tNo39.t0
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_4_0.scr43 \
        -background {#d9d9d9} -height 75 -highlightbackground {#d9d9d9} \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_4_0.scr43" "textScroll" vTcl:WidgetProc "Toplevel1" 1

    $site_4_0.scr43.01 configure -background white \
        -font font9 \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    ttk::style configure TButton -background #d9d9d9
    ttk::style configure TButton -foreground #000000
    ttk::style configure TButton -font TkDefaultFont
    ttk::button $site_4_0.tBu44 \
        -takefocus {} -text Convert 
    vTcl:DefineAlias "$site_4_0.tBu44" "btnConvert" vTcl:WidgetProc "Toplevel1" 1
    bind $site_4_0.tBu44 <Button-1> {
        lambda e: btnConvert_1click(e)
    }
    place $site_4_0.scr43 \
        -in $site_4_0 -x 10 -y 10 -width 825 -relwidth 0 -height 724 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.tBu44 \
        -in $site_4_0 -x 380 -y 750 -anchor nw -bordermode ignore 
    frame $top.tNo39.t1 \
        -background {#d9d9d9} -highlightbackground {#d9d9d9} \
        -highlightcolor black 
    vTcl:DefineAlias "$top.tNo39.t1" "TNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.tNo39 add $top.tNo39.t1 \
        -padding 0 -sticky nsew -state normal -text {Email   } -image {} \
        -compound left -underline -1 
    set site_4_1  $top.tNo39.t1
    ttk::style configure TButton -background #d9d9d9
    ttk::style configure TButton -foreground #000000
    ttk::style configure TButton -font TkDefaultFont
    ttk::button $site_4_1.tBu40 \
        -takefocus {} -text Tbutton 
    vTcl:DefineAlias "$site_4_1.tBu40" "myanchor" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_1.tBu40 \
        -in $site_4_1 -x 720 -y 700 -anchor nw -bordermode ignore 
    ttk::style configure TButton -background #d9d9d9
    ttk::style configure TButton -foreground #000000
    ttk::style configure TButton -font TkDefaultFont
    ttk::button $top.tBu46 \
        -takefocus {} -text Exit 
    vTcl:DefineAlias "$top.tBu46" "btnExit" vTcl:WidgetProc "Toplevel1" 1
    bind $top.tBu46 <Button-1> {
        lambda e: btnExit(e)
    }
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tNo39 \
        -in $top -x 20 -y 40 -width 854 -relwidth 0 -height 821 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu46 \
        -in $top -x 780 -y 880 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

#############################################################################
## Binding tag:  _TopLevel

bind "_TopLevel" <<Create>> {
    if {![info exists _topcount]} {set _topcount 0}; incr _topcount
}
bind "_TopLevel" <<DeleteWindow>> {
    if {[set ::%W::_modal]} {
                vTcl:Toplevel:WidgetProc %W endmodal
            } else {
                destroy %W; if {$_topcount == 0} {exit}
            }
}
bind "_TopLevel" <Destroy> {
    if {[winfo toplevel %W] == "%W"} {incr _topcount -1}
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top37 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
