/* viXra prefill - run in the browser console on https://fs23.formsite.com/viXra/form2/index.html
 * Fills text/select/radio fields ONLY. Deliberately does NOT:
 *   - fill the contact e-mail,
 *   - choose the local PDF file,
 *   - tick any rights/ownership declaration,
 *   - click submit.
 * Those four actions are the author's alone.
 */
(function () {
  var V = {"RESULT_RadioButton-5": "Radio-0", "RESULT_TextField-8": "https://kiloiam.github.io/labor-value-theory-preprint/paper-vixra.pdf", "RESULT_RadioButton-10": "Radio-32", "RESULT_TextField-12": "The Labor Theory of Value as a Historical Category: The Contemporary Crisis of Value", "RESULT_TextField-14": "Didgeridoo", "RESULT_TextArea-16": "Grounding its analysis in historical materialism, this article delineates the historical limits of the labor theory of value (LTV) and analyzes the structural crisis of the law of value under conditions of contemporary automated production. This article maintains that the LTV is not a universal economic principle applicable to all social formations; Rather, it emerges as a historically specific theory, grounded in wage labor, socially necessary labor time, and the universality of commodity exchange. On this basis, a revised value model incorporating automated technological capital is constructed. The paper demonstrates that as automated systems become capable in principle of performing productive functions independently of living labor, variable capital is systematically and irreversibly expelled from the production process. Accordingly, the process of surplus-value production has been tending towards its exhaustion; this process culminates in a fundamental breakdown of the value-category and the commodity-form which depends on it. In this context, profit no longer emerges as the result of valorization. Instead, profit becomes transmuted into a \"negative political cost of social stabilization under private property relations\" (P) needed for the maintenance of the institutional shell (integument) of private property. The article further elaborates on the \"four-fold impossibility\" of commodity society's self-repair. In doing so, it exposes an irreversible internal rupture in the value-structure. It concludes that the apparent obsolescence of the LTV does not refute the theory but rather indicates that commodity society has reached its historical endpoint. Thus, the central issue in the post-value-category era lies in the historical reconfiguration of production relations: namely, liberating automated productive capacities from the fetters of private appropriation and reorienting them toward a system aimed at the socialized organization of use-value. This analysis provides a theoretical criterion for understanding the specificity of the contemporary capitalist crisis and the direction of future social transformation.", "RESULT_TextField-17": "10", "RESULT_TextField-19": "CC BY 4.0. Online preprint, not peer reviewed. DOI 10.5281/zenodo.24270266.", "RESULT_TextArea-21": "The author publishes under the real English name Didgeridoo (not a pseudonym). This is an online preprint already deposited at Zenodo under DOI 10.5281/zenodo.24270266 and licensed CC BY 4.0; it is not peer reviewed and has not been published in a journal. The canonical full text is at https://kiloiam.github.io/labor-value-theory-preprint/ . The final page of the attached PDF carries the English title, English abstract, licence, DOIs and canonical links, because viXra does not place author-site links on its own pages. Please do not publish my e-mail address."};
  var filled = [], missing = [];
  Object.keys(V).forEach(function (name) {
    var list = document.getElementsByName(name);
    if (!list.length) { missing.push(name); return; }
    var el = list[0];
    if (el.tagName === 'SELECT') {
      el.value = V[name];
    } else if (el.type === 'radio') {
      var hit = false;
      for (var i = 0; i < list.length; i++) {
        if (list[i].value === V[name]) { list[i].checked = true; hit = true; }
      }
      if (!hit && list.length) { list[0].checked = true; }
    } else {
      el.value = V[name];
    }
    try {
      el.dispatchEvent(new Event('input',  {bubbles:true}));
      el.dispatchEvent(new Event('change', {bubbles:true}));
    } catch (e) {}
    filled.push(name);
  });

  // PDF submission method = Upload (Radio-0), checked explicitly.
  var method = document.getElementsByName('RESULT_RadioButton-5');
  for (var j = 0; j < method.length; j++) {
    method[j].checked = (method[j].value === 'Radio-0');
  }
  if (filled.indexOf('RESULT_RadioButton-5') < 0) filled.push('RESULT_RadioButton-5');

  // Highlight the only field the author must fill personally.
  var email = document.getElementsByName('RESULT_TextField-3')[0];
  if (email) {
    email.value = '';
    email.style.border = '3px solid #c0392b';
    email.style.background = '#fff7f5';
    email.setAttribute('placeholder', 'ENTER YOUR CONTACT E-MAIL HERE (viXra does not publish it)');
    email.focus();
  }
  var file = document.getElementsByName('RESULT_FileUpload-6')[0];
  if (file) { file.style.outline = '3px solid #c0392b'; }

  console.log('[viXra] auto-filled ' + filled.length + ' fields:', filled.join(', '));
  if (missing.length) console.warn('[viXra] fields not found:', missing.join(', '));
  console.log('[viXra] STILL TO DO BY THE AUTHOR:');
  console.log('  1. Enter your contact e-mail (highlighted). viXra states it is NOT published.');
  console.log('  2. Select paper-vixra.pdf in the highlighted file field.');
  console.log('  3. Confirm the AI-assistance condition: the form requires a human-written article.');
  console.log('     If AI assistance was used, go to https://ai.viXra.org instead.');
  console.log('  4. Read the rights declaration and click Submit yourself. This is permanent.');
})();
