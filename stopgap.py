a = """
<!DOCTYPE html>
<html>

<style>
.hide {
    display: none }
</style>

<div class="tab">
    <button class="tablinks" onclick="openCity(event, 'Lawyer')">Lawyer</button>
    <button class="tablinks" onclick="openCity(event, 'Practise')">Practise</button>
</div>

<div id="Lawyer" class = "tabcontent">
    <form action="/Lawyer" method = "post">
        First name: <input type="text" name="FirstName"><br>
        Last name: <input type="text" name="LastName"><br>
        PostCode: <input type="text" name="PostCode"><br>
        Specialty: <input type="text" name="Accreditation"><br>
        <input type="submit" value="Submit">
    </form>
</div>

<div id="Practise" class = "tabcontent hide" display: none>
    <form action="/Practise" method = "post">
        Practise Name: <input type="text" name="FirstName"><br>
        PostCode: <input type="text" name="PostCode"><br>
        Specialty: <input type="text" name="Accreditation"><br>
        <input type="submit" value="Submit">
    </form>
</div>

<script>
function openCity(evt, tabname) {
    var i, tabcontent, tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    document.getElementById(tabname).style.display = "block";
}
</script>

</html> 
"""
