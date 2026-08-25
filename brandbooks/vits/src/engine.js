<script>
(function(){
  var deck=document.getElementById('scaler');
  var slides=[].slice.call(deck.querySelectorAll('.slide'));
  var N=slides.length, cur=0, zoom=null;      // zoom null = fit
  var NAMES=window.__NAMES__, GROUPS=window.__GROUPS__;
  var stage=document.getElementById('stage');

  if(/[?&]thumb=1/.test(location.search)) document.documentElement.classList.add('thumbonly');

  function pad2(n){return (n<10?'0':'')+n;}

  function fitScale(){
    var pad=46, r=stage.getBoundingClientRect();
    return Math.max(.05, Math.min((r.width-pad*2)/1920,(r.height-pad*2)/1080));
  }
  function apply(){
    var s = (zoom===null) ? fitScale() : zoom;
    deck.style.transform='translate(-50%,-50%) scale('+s+')';
    var pctEl=document.getElementById('zpct');
    if(pctEl) pctEl.textContent=Math.round(s*100)+'%';
    document.getElementById('nav').classList.toggle('zoomed', zoom!==null);
  }
  window.addEventListener('resize',apply); apply();

  /* ------------------------------------------------------------ dot rail */
  var dots=document.getElementById('dots');
  (function(){
    var f=document.createDocumentFragment();
    for(var i=0;i<N;i++){
      var b=document.createElement('button');
      b.className='dot-i'; b.dataset.i=i;
      b.title=(i+1)+'. '+String(NAMES[i]).replace(/&middot;/g,'.');
      b.setAttribute('aria-label','Go to page '+(i+1));
      b.onclick=(function(k){return function(){show(k)}})(i);
      f.appendChild(b);
    }
    dots.appendChild(f);
  })();

  function show(i){
    i=Math.max(0,Math.min(N-1,i));
    slides.forEach(function(s,k){
      s.classList.remove('on','pre','post');
      if(k<i) s.classList.add('pre'); else if(k>i) s.classList.add('post');
    });
    var el=slides[i]; el.classList.remove('on'); void el.offsetWidth; el.classList.add('on');
    cur=i;
    document.getElementById('ncur').textContent=pad2(i+1);
    document.getElementById('nname').innerHTML=NAMES[i];
    document.getElementById('prev').disabled=(i===0);
    document.getElementById('next').disabled=(i===N-1);
    [].forEach.call(dots.children,function(d,k){
      var on=(k===i); d.classList.toggle('on',on); d.textContent=on?pad2(i+1):'';
      if(on) d.scrollIntoView({block:'nearest',inline:'center'});
    });
    if(history.replaceState) history.replaceState(null,'','#p'+(i+1));
  }
  window.__go=show;

  document.getElementById('prev').onclick=function(){show(cur-1)};
  document.getElementById('next').onclick=function(){show(cur+1)};
  document.getElementById('btnHome').onclick=function(){show(0)};

  /* ---------------------------------------------------------------- zoom */
  var STEPS=[.25,.4,.55,.7,.85,1,1.25,1.5,2,3];
  function nearest(){ var s=(zoom===null)?fitScale():zoom, b=0;
    for(var i=0;i<STEPS.length;i++) if(Math.abs(STEPS[i]-s)<Math.abs(STEPS[b]-s)) b=i; return b; }
  document.getElementById('zin').onclick=function(){ zoom=STEPS[Math.min(STEPS.length-1,nearest()+1)]; apply(); };
  document.getElementById('zout').onclick=function(){ zoom=STEPS[Math.max(0,nearest()-1)]; apply(); };
  document.getElementById('zpct').onclick=function(){ zoom=1; apply(); };
  document.getElementById('zfit').onclick=function(){ zoom=null; apply(); };

  /* -------------------------------------------------------------- scroll */
  var lock=false;
  window.addEventListener('wheel',function(e){
    if(document.getElementById('sheetlist').classList.contains('open')) return;
    if(zoom!==null) return;                    // zoomed in, let the page be inspected
    if(Math.abs(e.deltaY)<12||lock) return;
    lock=true; setTimeout(function(){lock=false},400);
    show(cur+(e.deltaY>0?1:-1));
  },{passive:true});

  /* ------------------------------------------------------------ keyboard */
  document.addEventListener('keydown',function(e){
    var k=e.key;
    if(k==='ArrowRight'||k==='PageDown'||k===' '){e.preventDefault();show(cur+1)}
    else if(k==='ArrowLeft'||k==='PageUp'){e.preventDefault();show(cur-1)}
    else if(k==='Home'){show(0)} else if(k==='End'){show(N-1)}
    else if(k==='0'){zoom=null;apply()}
    else if(k==='g'||k==='G'){toggleGrid()}
    else if(k==='p'||k==='P'){openPm()}
    else if(k==='Escape'){closeAll()}
  });

  /* ---------------------------------------------------------- page grid */
  var built=false;
  function buildGrid(){
    if(built) return; built=true;
    var g=document.getElementById('slgrid'), lastG=null, frag=document.createDocumentFragment();
    for(var i=0;i<N;i++){
      if(GROUPS[i]!==lastG){
        var gh=document.createElement('div'); gh.className='slgroup';
        gh.textContent=GROUPS[i]; frag.appendChild(gh); lastG=GROUPS[i];
      }
      var d=document.createElement('div'); d.className='slth';
      var fr=document.createElement('div'); fr.className='slfr';
      var cl=slides[i].querySelector('.pg').cloneNode(true);
      cl.classList.add('mini'); cl.style.transform='scale(.13)';
      [].forEach.call(cl.querySelectorAll('.rv'),function(x){
        x.classList.remove('rv'); x.style.opacity=1; x.style.transform='none'; });
      fr.appendChild(cl);
      var cap=document.createElement('div'); cap.className='slcap';
      cap.innerHTML='<b>'+pad2(i+1)+'</b> &nbsp;'+NAMES[i];
      d.appendChild(fr); d.appendChild(cap);
      d.onclick=(function(k){return function(){show(k);toggleGrid(false)}})(i);
      frag.appendChild(d);
    }
    g.appendChild(frag);
    requestAnimationFrame(rescale);
  }
  function rescale(){
    [].forEach.call(document.querySelectorAll('#slgrid .slfr'),function(fr){
      var m=fr.querySelector('.mini');
      if(m) m.style.transform='scale('+(fr.clientWidth/1920)+')';
    });
  }
  window.addEventListener('resize',rescale);
  function toggleGrid(force){
    var s=document.getElementById('sheetlist');
    var open=(force===undefined)?!s.classList.contains('open'):force;
    if(open){buildGrid();s.classList.add('open');document.getElementById('nav').classList.add('hide');}
    else{s.classList.remove('open');document.getElementById('nav').classList.remove('hide');}
  }
  document.getElementById('btnGrid').onclick=function(){toggleGrid()};
  document.getElementById('slClose').onclick=function(){toggleGrid(false)};

  /* --------------------------------------------------------------- print */
  var pmSize={w:'1920px',h:'1080px',s:'1'}, pmRange='all';
  function openPm(){document.getElementById('pm').classList.add('open')}
  function closeAll(){
    document.getElementById('pm').classList.remove('open');
    toggleGrid(false);
  }
  document.getElementById('btnPrint').onclick=openPm;
  document.getElementById('pmCancel').onclick=function(){document.getElementById('pm').classList.remove('open')};
  [].forEach.call(document.querySelectorAll('#optSize .opt'),function(o){
    o.onclick=function(){
      [].forEach.call(document.querySelectorAll('#optSize .opt'),function(x){x.classList.remove('sel')});
      o.classList.add('sel'); pmSize={w:o.dataset.w,h:o.dataset.h,s:o.dataset.s};};
  });
  [].forEach.call(document.querySelectorAll('#optRange .opt'),function(o){
    o.onclick=function(){
      [].forEach.call(document.querySelectorAll('#optRange .opt'),function(x){x.classList.remove('sel')});
      o.classList.add('sel'); pmRange=o.dataset.r;};
  });
  document.getElementById('pmGo').onclick=function(){
    var root=document.getElementById('printroot'); root.innerHTML='';
    var list=(pmRange==='one')?[cur]:slides.map(function(_,i){return i});
    list.forEach(function(i){
      var sh=document.createElement('div'); sh.className='sheet';
      var cl=slides[i].querySelector('.pg').cloneNode(true);
      cl.style.transform='none';
      [].forEach.call(cl.querySelectorAll('.rv'),function(x){x.classList.remove('rv')});
      sh.appendChild(cl); root.appendChild(sh);
    });
    document.getElementById('psize').textContent=
      '@page{size:'+pmSize.w+' '+pmSize.h+';margin:0}'+
      ':root{--pw:'+pmSize.w+';--ph:'+pmSize.h+';--ps:'+pmSize.s+'}';
    document.getElementById('pm').classList.remove('open');
    setTimeout(function(){window.print()},140);
  };
  window.addEventListener('afterprint',function(){document.getElementById('printroot').innerHTML=''});

  document.getElementById('ntot').textContent=pad2(N);
  var m=(location.hash||'').match(/^#p(\d+)$/);
  show(m?Math.min(N,parseInt(m[1],10))-1:0);
  setTimeout(function(){document.getElementById('hint').classList.add('hide')},5600);
})();
</script>
