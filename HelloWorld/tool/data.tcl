#resid start from 1(real pdb)
#resid start from 0(vmd pdb)
#vmd -dispdev -eof <data.tcl>&

set res_amino [list ALA ARG ASN ASP CYS GLU GLN GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL]
set pdblist name
mol new ./static/files/data.pdb type pdb

#### 获取所有原子组成的变量sel ####
set sel [atomselect top "all"]
#### 获取所有链名 ####
set name_chain [lsort -unique [$sel get chain]]
#set residue [$sel get residue]
#set residue [lsort -unique -integer $residue]

foreach ichain $name_chain {
    #### 获取当前链上所有的原子 ####
    set ato [atomselect top "chain $ichain"]
    #### 获取当前链上所有原子的resid ####
    set resid [$ato get resid]

    #### 循环遍历每个残基 ####
    foreach ires $resid  {
        #### 列出该残基所有的原子 ####
        set seli [atomselect top "resid $ires and chain $ichain"]
        #### 列出该残基的名称 ####
        set resname [$seli get resname]

        set a [lsearch $res_amino [lindex $resname 1]]
        if {$a==19} {
            set residue VAL
        } elseif {$a==18} {
            set residue TYR
        } elseif {$a==17} {
            set residue TRP
        } elseif {$a==16} {
            set residue THR
        } elseif {$a==15} {
            set residue SER
        } elseif {$a==14} {
            set residue PRO
        } elseif {$a==13} {
            set residue PHE
        } elseif {$a==12} {
            set residue MET
        } elseif {$a==11} {
            set residue LYS
        } elseif {$a==10} {
            set residue LEU
        } elseif {$a==9} {
            set resdiue ILE
        } elseif {$a==8} {
            set residue HIS
        } elseif {$a==7} {
            set residue GLY
        } elseif {$a==6} {
            set residue GLN
        } elseif {$a==5} {
            set residue GLU
        } elseif {$a==4} {
            set residue CYS
        } elseif {$a==3} {
            set residue ASP
        } elseif {$a==2} {
            set residue ASN
        } elseif {$a==1} {
            set residue ARG
        } elseif {$a==0} {
            set residue ALA
        }
        #### 获取该残基周围6.5埃以内的所有残基 ####
        set res [atomselect top "within 6.5 of resid $ires"]
        #### 获取这些满足条件的残基所在的链的名称,resid,resname ####
        foreach r $res {
            
            ###cha是链的名称###
            set cha [lsort -unique [$r get chain]]
            ###resn是残基名###
            set resn [$r get resname]
            ###residu是满足条件的残基的residue编号
            set residu [lsort -unique [$r get residue]]
            foreach resu $residu {
                set at [atomselect top "residue $resu"]
                set resd [lsort -unique [$at get resid]]
                set cha [lsort -unique [$at get chain]]
                set resout1 [atomselect top "(resid $resd and chain $cha)or(resid $ires and chain $ichain)"]
                #set resout2 [atomselect top "(resid $ires and chain $ichain)"]
                set b [lsearch $resn [lindex $resname 1]]
                set e 1
                set check1 [expr $ires+$e]
                set check2 [expr $resd+$e]
                if $b==-1||$check1==$resd||$check2==$ires||$ires==$resd {
                    puts wrongselection!
                } else {
                    #ichain:中心残基链
                    set pdblist $ichain
                    #ires：中心残基resid
                    append pdblist _$ires
                    #cha：非中心残基链名
                    append pdblist _$cha
                    #resd：非中心残基resid
                    append pdblist _$resd
                    #puts $pdblist
                    $resout1  writepdb ./static/files/side/$pdblist.pdb
                }
            }
        }
    }
}
#if  {
 #   set resd [lsort -unique [$r get resid]]
  #  set resn [$r get resname]
    #puts resn
    #puts resd
    #puts 1234
    #set b [lsearch $resn [lindex $resname 1]]
    #set resout [atomselect top "(resid $ires and chain $ichain) or (resid $resd and chain $cha)"]
    #puts $b
    #if $b!=-1 {
    #    set pdblist $ichain
    #    append pdblist _$ires
    #    append pdblist _$cha
    #    append pdblist _$resd
     #   $resout writepdb ../static/files/$pdblist.pdb
    #}
#}




#        set residout [$res get resid]
#        set residout [lsort -unique -integer $residout]
#        foreach iresidout $residout {
 #           set isel [atomselect top "resid $iresidout"]
  #          set iresname [$isel get resname]
   #         if {$iresidout != $ires} {
    #            set resout [atomselect top "resid $ires or resid $iresidout "]
     #           set num [llength $iresname]
      #          if {$num > 1} {
       #             set iresname [lindex $iresname 1]
        #        }
         #       set pdblist data
          #      append pdblist _$residue
           #     append pdblist _$ires
            #    append pdblist _$iresname
             #   append pdblist _$iresidout
              #  $resout writepdb ./data/$pdblist.pdb 
            #}

        #}

