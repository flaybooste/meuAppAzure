(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{45:function(e,t,n){e.exports=n(61)},50:function(e,t,n){},51:function(e,t,n){},56:function(e,t,n){},61:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),c=n(15),l=n.n(c),o=(n(50),n(51),n(6)),i=n(84),u=function(){return a.createElement(i.a,{fixed:!0},a.createElement("div",null,a.createElement("h1",null,"Home")))},m=n(30),s=n.n(m),E=n(40),d=n(33),f=(n(56),n(93)),p=n(86),h=n(87),v=n(63),b=function(){var e=Object(a.useState)(),t=Object(d.a)(e,2),n=t[0],c=t[1],l=Object(a.useState)(!0),o=Object(d.a)(l,2),u=o[0],m=o[1];function b(){return(b=Object(E.a)(s.a.mark((function e(){var t,n;return s.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,fetch("https://dududisse3.azurewebsites.net/api",{method:"GET",mode:"cors",headers:{"Content-Type":"application/json"}});case 2:return t=e.sent,e.next=5,t.json();case 5:n=e.sent,c(n),m(!1);case 8:case"end":return e.stop()}}),e)})))).apply(this,arguments)}return Object(a.useEffect)((function(){return function(){b.apply(this,arguments)}(),n}),[]),n?r.a.createElement("div",null,n.map((function(e){return r.a.createElement(i.a,{fixed:!0},r.a.createElement(f.a,{in:!u,timeout:700},r.a.createElement(h.a,{item:!0,xs:!0},r.a.createElement(v.a,{elevation:2},r.a.createElement("div",{id:"posts"},r.a.createElement("div",{id:"post"},r.a.createElement("h2",null,e.title),console.log(e),r.a.createElement("label",{id:"desc"},e.descp)))))),r.a.createElement("br",null))}))):r.a.createElement(f.a,{in:u,timeout:700},r.a.createElement(i.a,{fixed:!0},r.a.createElement(p.a,null)))},w=function(){return r.a.createElement("div",null,r.a.createElement(o.c,null,r.a.createElement(o.a,{exact:!0,path:"/",component:b}),r.a.createElement(o.a,{path:"/about",component:u})))},x=n(18),j=function(){return r.a.createElement("div",null)},g=n(88),O=n(94),k=n(89),y=n(90),B=n(91),G=n(92),S=n(41),J=n.n(S),N=Object(g.a)((function(e){return Object(O.a)({root:{flexGrow:1},menuButton:{marginRight:e.spacing(2)},title:{flexGrow:1}})}));function T(){var e=N();return r.a.createElement("div",{className:e.root},r.a.createElement(k.a,{position:"static",color:"transparent"},r.a.createElement(y.a,null,r.a.createElement(B.a,{variant:"h6",className:e.title},r.a.createElement(x.b,{to:"/"},r.a.createElement(J.a,null))),r.a.createElement(G.a,{color:"inherit"},r.a.createElement(x.b,{to:"/about"},"About")))))}var W=function(){return r.a.createElement(x.a,null,r.a.createElement("div",null,r.a.createElement(T,null),r.a.createElement(w,null),r.a.createElement(j,null)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(W,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[45,1,2]]]);
//# sourceMappingURL=main.8d945ab2.chunk.js.map